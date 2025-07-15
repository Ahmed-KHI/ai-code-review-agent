import chainlit as cl
import importlib
import sys


if 'code_review_agent' in sys.modules:
    importlib.reload(sys.modules['code_review_agent'])

from code_review_agent import review_code, model

@cl.on_chat_start
async def start():
    """Initialize the chat session and check API status."""
    if model is None:
        await cl.Message(
            content="❌ **API Key Error**: Gemini model not initialized.\n\n"
                   "Please ensure your API key is valid:\n"
                   "1. Go to https://aistudio.google.com/app/apikey\n"
                   "2. Create a new API key\n"
                   "3. Update your .env file: `GEMINI_API_KEY=your_new_key`\n"
                   "4. Restart the application"
        ).send()
    else:
        await cl.Message(
            content="✅ **Code Review Agent Ready!**\n\n"
                   "Send me any code and I'll provide a comprehensive review including:\n"
                   "• Code summary and functionality\n"
                   "• Best practices analysis\n"
                   "• Issues and improvements\n"
                   "• Security recommendations\n"
                   "• Quality rating (1-10)"
        ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    code = message.content.strip()
    
    if not code:
        await cl.Message(content="❌ Please provide some code to review.").send()
        return
    
    if model is None:
        await cl.Message(
            content="❌ **API Error**: Gemini model not available. Please check your API key and restart the application."
        ).send()
        return
    
    await cl.Message(content="🔍 **Reviewing your code...**").send()
    
    try:
        result = review_code(code)
        await cl.Message(content=result).send()
    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg or "API key not valid" in error_msg:
            await cl.Message(
                content="❌ **API Key Invalid**: Your Gemini API key is not working.\n\n"
                       "Please:\n"
                       "1. Get a new API key from https://aistudio.google.com/app/apikey\n"
                       "2. Update your .env file\n"
                       "3. Restart the application"
            ).send()
        else:
            await cl.Message(content=f"❌ **Error**: {error_msg}").send()
