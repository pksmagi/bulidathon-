# 📌 QUICK REFERENCE CARD - Buildathon Project

## 🎯 Your Project
**Customer Support System with Three Sequential CrewAI Agents**

📂 Location: `C:\Users\pksma\OneDrive\Desktop1\buildathon-support-crew`

---

## 🚀 PUSH TO GITHUB IN 3 STEPS

### Step 1: Create GitHub Repo
**URL:** https://github.com/new
- Name: `buildathon-support-crew`
- Visibility: **PUBLIC**

### Step 2: Get Personal Access Token
**URL:** https://github.com/settings/tokens
- **Generate new token (classic)**
- Scope: `repo` ✓
- **COPY THE TOKEN**

### Step 3: Push Code
```powershell
cd "C:\Users\pksma\OneDrive\Desktop1\buildathon-support-crew"
git push -u origin main
```
- Username: `pksmagi`
- Password: Paste token from Step 2

---

## 📚 Important Files to Read

| File | Purpose | Time |
|------|---------|------|
| **START_HERE.md** | Overview | 2 min |
| **PUSH_TO_GITHUB.md** | Push instructions | 5 min |
| **SUBMISSION_CHECKLIST.md** | Verification | 3 min |
| **QUICKSTART.md** | Run app locally | 5 min |
| **README.md** | Full docs | 10 min |

👉 **Start with:** `START_HERE.md`

---

## 🔑 Important Links

- 📝 Create Repo: https://github.com/new
- 🔐 Get Token: https://github.com/settings/tokens
- 🤖 OpenAI Keys: https://platform.openai.com/api-keys
- 🔍 Serper Keys: https://serper.dev
- ⚠️ Revoke Old Key: https://platform.openai.com/account/api-keys

---

## 🤖 Three Agents

| Agent | Role | Tool |
|-------|------|------|
| **1. Assistant** | Direct answers | Knowledge |
| **2. Web Search** | Internet search | Serper API |
| **3. Entry** | Save to file | File system |

**Process:** Sequential (each uses previous output)

---

## ✅ All Requirements Met

- ✅ Three agents
- ✅ Sequential process
- ✅ Streamlit UI
- ✅ Web search
- ✅ File storage
- ✅ Single app.py file
- ✅ Environment variables
- ✅ Both answers shown

---

## 🧪 Run App Locally

```powershell
# Activate venv
.\venv\Scripts\Activate.ps1

# Set API keys
$env:OPENAI_API_KEY="your-key"
$env:SERPER_API_KEY="your-key"

# Run app
streamlit run app.py
```

Browser: `http://localhost:8501`

---

## 📋 Project Contents

```
app.py                     ← Main application
requirements.txt          ← Dependencies
venv/                     ← Virtual environment
START_HERE.md            ← 👈 Read first
PUSH_TO_GITHUB.md        ← Push instructions
SUBMISSION_CHECKLIST.md  ← Requirements check
README.md                ← Full documentation
.gitignore               ← Security
.env.example             ← API key template
```

---

## ⏱️ Timeline to Submission

| Step | Action | Time |
|------|--------|------|
| 1 | Read START_HERE.md | 2 min |
| 2 | Read PUSH_TO_GITHUB.md | 5 min |
| 3 | Create GitHub repo | 2 min |
| 4 | Get Personal Access Token | 1 min |
| 5 | Push code | 1 min |
| 6 | Verify on GitHub | 1 min |
| **Total** | **Ready to submit!** | **~12 min** |

---

## 🎓 Git Commands

```bash
# Check status
git status

# See commits
git log --oneline

# Push to GitHub
git push -u origin main

# Check remote
git remote -v
```

---

## 🔒 Security Reminders

⚠️ **Never** commit `.env` file with real keys
⚠️ **Always** use environment variables
⚠️ **Revoke** exposed API keys immediately
✅ `.gitignore` already configured
✅ `.env.example` provided as template

---

## 🆘 If You Get Stuck

1. **Can't push to GitHub?**
   → Read PUSH_TO_GITHUB.md

2. **GitHub issues?**
   → Read GITHUB_SETUP.md

3. **Can't run app?**
   → Read QUICKSTART.md or README.md

4. **Buildathon questions?**
   → Read SUBMISSION_CHECKLIST.md

---

## 🎉 You're Ready!

✅ Code complete
✅ Documentation complete
✅ Git repository ready
✅ All requirements met

**Next step:** Read `START_HERE.md`

**GitHub link (after push):**
```
https://github.com/pksmagi/buildathon-support-crew
```

---

## 📞 Quick Reference

- **Project Location:** C:\Users\pksma\OneDrive\Desktop1\buildathon-support-crew
- **Main File:** app.py (~350 lines)
- **Tech Stack:** Python + CrewAI + Streamlit
- **Deployment:** GitHub
- **Status:** Ready to submit ✅

---

Good luck! 🚀
