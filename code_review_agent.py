from dotenv import load_dotenv
import os
import google.generativeai as genai
from typing import Optional

# Load environment variables
load_dotenv()

def initialize_gemini() -> Optional[genai.GenerativeModel]:
    """Initialize Gemini API with proper error handling."""
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    if not api_key.startswith("AIzaSy"):
        raise ValueError("Invalid API key format. Gemini API keys should start with 'AIzaSy'")
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Test the API key with a simple request
        test_response = model.generate_content("Test")
        if not test_response.text:
            raise Exception("API key test failed - empty response")
            
        print(f"✅ Gemini API initialized successfully with model: gemini-1.5-flash")
        return model
    except Exception as e:
        error_msg = str(e).lower()
        if "api_key_invalid" in error_msg or "api key not valid" in error_msg or "invalid api key" in error_msg:
            raise ConnectionError("API key is invalid or expired. Please get a new one from https://aistudio.google.com/app/apikey")
        else:
            raise ConnectionError(f"Failed to initialize Gemini API: {str(e)}")

# Initialize the model
try:
    model = initialize_gemini()
except Exception as e:
    print(f"Error initializing Gemini: {e}")
    model = None

REVIEW_PROMPT = """
You are a senior software engineer and expert code reviewer with 15+ years of experience.

Please provide a comprehensive code review with the following structure:

## 🔍 **CODE ANALYSIS**
1. **Summary**: What does this code do?
2. **Algorithm Complexity**: Time and space complexity analysis
3. **Architecture**: Overall design and structure assessment

## ✅ **STRENGTHS**
- List what the code does well
- Best practices followed
- Good design patterns used

## ⚠️ **ISSUES IDENTIFIED**
- **Security**: Any security vulnerabilities (with line numbers)
- **Performance**: Inefficiencies or bottlenecks (with line numbers)
- **Style**: Code style violations (with line numbers)
- **Logic**: Potential bugs or edge cases (with line numbers)

## 🚀 **IMPROVEMENT SUGGESTIONS**
1. **Refactoring**: How to improve code structure
2. **Performance**: Optimization opportunities
3. **Security**: Security hardening recommendations
4. **Testing**: What tests should be added

## 📊 **QUALITY METRICS**
- **Overall Quality**: X/10
- **Security**: X/10
- **Performance**: X/10
- **Maintainability**: X/10
- **Readability**: X/10

## 🎯 **PRIORITY ACTIONS**
List the top 3 most important improvements to implement first.

---

CODE TO REVIEW:
```
{code}
```

Please provide detailed, actionable feedback with specific examples and code snippets where helpful.
"""

def review_code(code: str) -> str:
    """
    Review the provided code using Gemini AI.
    
    Args:
        code (str): The code to review
        
    Returns:
        str: The AI-generated code review
        
    Raises:
        ValueError: If code is empty or model is not initialized
        Exception: If API call fails
    """
    if not code or not code.strip():
        raise ValueError("Code cannot be empty")
    
    if model is None:
        raise ValueError("Gemini model not initialized. Please check your API key.")
    
    # Basic validation
    if len(code) > 10000:  # Limit code length
        raise ValueError("Code is too long. Please limit to 10,000 characters.")
    
    if len(code.strip()) < 10:  # Minimum meaningful code length
        raise ValueError("Code snippet is too short for meaningful review.")
    
    try:
        prompt = REVIEW_PROMPT.format(code=code)
        
        # Configure generation parameters for better output
        generation_config = genai.types.GenerationConfig(
            temperature=0.3,  # Lower temperature for more consistent reviews
            max_output_tokens=4000,  # Ensure detailed reviews
        )
        
        response = model.generate_content(prompt, generation_config=generation_config)
        
        if not response.text:
            raise Exception("Empty response from Gemini API")
        
        # Add metadata to the response
        review_header = f"**📅 Review Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        review_header += f"**📏 Code Length:** {len(code)} characters\n"
        review_header += f"**🤖 Reviewed by:** Code Review Agent\n\n---\n\n"
        
        return review_header + response.text
    
    except Exception as e:
        raise Exception(f"Failed to generate code review: {str(e)}")
