# 🤖 AI Code Review Agent

An intelligent code review assistant powered by Google's Gemini AI, built with Chainlit for an intuitive web interface.

## ✨ Features

- **🔍 Comprehensive Code Analysis**: Algorithm complexity, security vulnerabilities, performance bottlenecks
- **📊 Quality Metrics**: Multi-dimensional scoring (security, performance, maintainability, readability)
- **🎯 Actionable Feedback**: Specific line references and priority recommendations
- **🌐 Web Interface**: Clean, chat-based UI built with Chainlit
- **⚡ Real-time Reviews**: Instant feedback with detailed explanations
- **🔒 Secure**: API key validation and proper error handling

## 🛠️ Technology Stack

- **AI Model**: Google Gemini 1.5 Flash
- **Backend**: Python 3.8+
- **Frontend**: Chainlit
- **Environment Management**: python-dotenv

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ahmed-KHI/ai-code-review-agent.git
   cd ai-code-review-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your Gemini API key
   ```

4. **Run the application**
   ```bash
   chainlit run main.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8000`

## 🔧 Configuration

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## 📖 Usage

1. **Start the application** using `chainlit run main.py`
2. **Open the web interface** in your browser
3. **Paste your code** into the chat
4. **Get instant review** with detailed analysis and recommendations

### Example Review Output

```markdown
## 🔍 CODE ANALYSIS
- Summary: Function implements bubble sort algorithm
- Algorithm Complexity: O(n²) time, O(1) space
- Architecture: Simple iterative approach

## ⚠️ ISSUES IDENTIFIED
- Performance: Inefficient for large datasets (line 3-6)
- Style: Missing type hints (line 1)

## 🚀 IMPROVEMENT SUGGESTIONS
1. Consider using built-in sorted() function
2. Add input validation
3. Include docstring with examples

## 📊 QUALITY METRICS
- Overall Quality: 6/10
- Performance: 4/10
- Readability: 8/10
```

## 🏗️ Project Structure

```
ai-code-review-agent/
├── main.py                 # Chainlit web application
├── code_review_agent.py    # Core review logic
├── chainlit.md            # Welcome page content
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── .env                  # Your API keys (git-ignored)
├── .gitignore           # Git ignore rules
└── README.md           # This file
```

## 🔒 Security

- API keys are stored in environment variables
- Input validation prevents malicious code execution
- Error handling protects against API failures
- No code is stored or logged permanently

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛠️ Development

### Running in Development Mode

```bash
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
chainlit run main.py --auto-reload
```

### Testing

```bash
# Test the core functionality
python -c "from code_review_agent import review_code; print('✅ Import successful')"
```

## 📊 Performance

- **Average Response Time**: < 3 seconds
- **Supported Code Length**: Up to 10,000 characters
- **Concurrent Users**: Supports multiple simultaneous reviews
- **Accuracy**: Powered by Google's state-of-the-art Gemini AI

## 🔮 Future Enhancements

- [ ] Multiple file upload support
- [ ] Code syntax highlighting
- [ ] Review history and export
- [ ] Language-specific templates
- [ ] VS Code extension
- [ ] Team collaboration features

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Ahmed-KHI/ai-code-review-agent/issues) page
2. Create a new issue with detailed description
3. Join our community discussions

## 🌟 Show Your Support

If this project helps you, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🤝 Contributing code

---

**Made with ❤️ by [Muhammad Ahmed]**

*Helping developers write better code, one review at a time.*
