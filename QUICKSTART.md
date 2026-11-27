# Quick Start Guide - Customer Support Crew

## 🚀 Get Running in 5 Minutes

### 1. Navigate to Project
```bash
cd buildathon-support-crew
```

### 2. Activate Virtual Environment
**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Set Your API Keys
**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-key-here"
$env:SERPER_API_KEY="your-key-here"
```

**macOS/Linux:**
```bash
export OPENAI_API_KEY="your-key-here"
export SERPER_API_KEY="your-key-here"
```

### 4. Run the App
```bash
streamlit run app.py
```

### 5. Use the App
- Open browser to `http://localhost:8501`
- Type a support query (e.g., "How do I reset my password?")
- Click Submit
- Watch the three agents work sequentially
- View answers in the UI
- Check `answers.txt` for saved records

## 📋 What Each Agent Does

| Agent | Task | Tool |
|-------|------|------|
| **1. Assistant** | Answer directly | Knowledge base |
| **2. Web Search** | Search internet | Serper API |
| **3. Entry Agent** | Save to file | File system |

## 🔑 Get API Keys

1. **OpenAI Key**: https://platform.openai.com/api-keys
2. **Serper Key**: https://serper.dev (free tier available)

## ⚠️ Important

- Never share your API keys
- Never commit `.env` file
- Always use environment variables
- Keep `.env` in `.gitignore` (already done)

## 🆘 Troubleshooting

**"Module not found" error**
```bash
pip install crewai crewai-tools streamlit
```

**"API key not found" error**
- Double-check your environment variables are set
- Restart terminal after setting them

**Port 8501 already in use**
```bash
streamlit run app.py --server.port 8502
```

## 📂 Output

All queries and answers are saved to `answers.txt` in the project folder.

Enjoy! 🎉
