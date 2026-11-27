# 🤖 Customer Support System with CrewAI

A sophisticated customer support system built with **CrewAI** and **Streamlit** featuring three sequential agents that work together to answer customer queries.

## Features

- **Sequential Agent Architecture**: Three agents run one after another, each building on previous results
  1. **Assistant Agent** - Provides direct answers from training knowledge
  2. **Web Search Agent** - Searches the web for current information
  3. **Entry Agent** - Saves all interactions to a file for record-keeping

- **Streamlit Web Interface** - Clean, intuitive UI for customer queries
- **Persistent Storage** - All queries and answers saved to `answers.txt`
- **Secure API Management** - All API keys read from environment variables

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (from [platform.openai.com](https://platform.openai.com/api-keys))
- Serper API key for web search (from [serper.dev](https://serper.dev))

## Setup Instructions

### Step 1: Clone or Create Project

```bash
git clone <your-repo-url>
cd buildathon-support-crew
```

### Step 2: Create Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
pip install crewai crewai-tools streamlit
```

### Step 4: Set Up Environment Variables

**On macOS/Linux:**
```bash
export OPENAI_API_KEY="your-openai-key"
export SERPER_API_KEY="your-serper-key"
```

**On Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-openai-key"
$env:SERPER_API_KEY="your-serper-key"
```

**On Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-openai-key
set SERPER_API_KEY=your-serper-key
```

Alternatively, create a `.env` file (copy from `.env.example`) and use a tool like `python-dotenv`:
```bash
pip install python-dotenv
```

Then at the top of `app.py`, add:
```python
from dotenv import load_dotenv
load_dotenv()
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## Usage

1. **Enter a Query** - Type your customer support question in the input box
2. **Submit** - Click the "Submit" button
3. **Wait for Processing** - The three agents will work sequentially:
   - Agent 1 provides a direct answer
   - Agent 2 searches the web
   - Agent 3 saves everything to a file
4. **View Results** - Both answers are displayed in the UI
5. **Check Output** - The file `answers.txt` contains all interaction history

## Project Structure

```
buildathon-support-crew/
├── app.py                 # Main application file (all code in one file)
├── answers.txt           # Output file with all queries and answers
├── .gitignore            # Git ignore file
├── .env.example          # Example environment variables
├── venv/                 # Virtual environment (not committed)
└── README.md             # This file
```

## How It Works

### Sequential Process Flow

```
User Query
    ↓
[Agent 1: Assistant] → Direct Answer
    ↓
[Agent 2: Web Search] → Web Search Answer (uses previous output)
    ↓
[Agent 3: Entry Agent] → Saves to file + Returns both answers
    ↓
Display Results to User
```

### Agent Details

**Agent 1 - Customer Support Assistant**
- Answers queries directly from training knowledge
- No external tools
- Quick response based on existing knowledge

**Agent 2 - Web Search Assistant**
- Uses SerperDevTool for web search
- Provides current, up-to-date information
- Builds on the first agent's output

**Agent 3 - Entry Agent**
- Receives output from both previous agents
- Saves query + both answers to `answers.txt`
- Returns formatted results to the user

## Important Notes

⚠️ **Never commit API keys!**
- Always use environment variables
- Use `.env.example` as a template
- Add `.env` to `.gitignore` (already included)

⚠️ **API Key Setup**
- Ensure `OPENAI_API_KEY` and `SERPER_API_KEY` are set before running
- The app will check for these keys and show helpful error messages if missing

## Troubleshooting

**"OPENAI_API_KEY not set" error**
- Make sure you've set the environment variable before running the app
- Restart your terminal after setting environment variables

**"SERPER_API_KEY not set" error**
- Get a free API key from [serper.dev](https://serper.dev)
- Set it as an environment variable

**Virtual environment not activating**
- On Windows PowerShell, you may need to allow script execution:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

**Streamlit port already in use**
- Run on a different port:
  ```bash
  streamlit run app.py --server.port 8502
  ```

## Stopping the Application

Press `Ctrl + C` in the terminal where the app is running.

To deactivate the virtual environment:
```bash
deactivate
```

## Technologies Used

- **CrewAI** - Multi-agent framework for orchestrating AI agents
- **Streamlit** - Web UI framework for data applications
- **OpenAI GPT** - Language model for agent reasoning
- **Serper API** - Web search capability
- **Python 3.8+** - Programming language

## Next Steps & Enhancements

- Add database storage for query history
- Implement chat history/conversations
- Add authentication for multi-user support
- Create custom tools for specific domains
- Add rate limiting and cost tracking
- Implement better answer formatting and presentation
- Add feedback mechanism to rate answers

## License

This project is part of the Weekly Buildathon.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the `.env.example` file
3. Ensure all dependencies are installed with `pip list`
