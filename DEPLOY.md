# 📤 Deploy to GitHub

## Option 1: Using GitHub Web Interface (Easiest)

### Step 1: Create Repository on GitHub
1. Go to https://github.com/new
2. Enter repository name: `buildathon-support-crew`
3. Add description: "Customer Support System with Three Sequential CrewAI Agents"
4. Choose **Public** (so others can see it)
5. Click **Create repository**

### Step 2: Push from Command Line
After creating the repository, GitHub will show you these commands. Run them in your project folder:

```bash
cd C:\Users\pksma\OneDrive\Desktop1\buildathon-support-crew

# Remove old remote if it exists
git remote remove origin

# Add new remote
git remote add origin https://github.com/pksmagi/buildathon-support-crew.git

# Rename branch to main (if needed)
git branch -M main

# Push your code
git push -u origin main
```

When prompted for authentication:
- **Username**: Your GitHub username
- **Password**: Use a **Personal Access Token** (not your password)

### Step 3: Create a Personal Access Token
1. Go to https://github.com/settings/tokens
2. Click **Generate new token** → **Generate new token (classic)**
3. Name it: `buildathon-deployment`
4. Select scopes: `repo` (all)
5. Click **Generate token**
6. **Copy the token** (you won't see it again)
7. Use this token as your password when git prompts

---

## Option 2: Using GitHub CLI (If gh is Installed)

```bash
cd C:\Users\pksma\OneDrive\Desktop1\buildathon-support-crew

# Authenticate
gh auth login

# Create and push repository
gh repo create buildathon-support-crew --public --source=. --remote=origin --push
```

---

## Option 3: Using Git with SSH Keys (Advanced)

If you've already set up SSH keys on GitHub:

```bash
cd C:\Users\pksma\OneDrive\Desktop1\buildathon-support-crew

git remote remove origin
git remote add origin git@github.com:pksmagi/buildathon-support-crew.git
git branch -M main
git push -u origin main
```

---

## ✅ Verify Your Repository

Once pushed, verify everything is there:
1. Go to https://github.com/pksmagi/buildathon-support-crew
2. Check that you see:
   - `app.py` ✅
   - `README.md` ✅
   - `QUICKSTART.md` ✅
   - `requirements.txt` ✅
   - `.gitignore` ✅
   - `.env.example` ✅
3. Check the commit history shows your commits

---

## 🔐 Security Reminder

Make sure your `.env` file (if you created one) is NOT in the repository:
```bash
git status
```

You should see `.env` listed as ignored. If it shows up, it means `.gitignore` didn't catch it. 

**Never commit `.env` with real API keys!**

---

## 📋 What Gets Pushed

```
buildathon-support-crew/
├── app.py                 ✅
├── requirements.txt       ✅
├── README.md             ✅
├── QUICKSTART.md         ✅
├── DEPLOY.md             ✅
├── .env.example          ✅
├── .gitignore            ✅
└── [.git folder]         ✅ (Git history)

NOT pushed (intentionally):
├── venv/                 ❌ (virtual environment)
├── .env                  ❌ (actual API keys)
├── answers.txt           ❌ (output file)
└── __pycache__/          ❌ (Python cache)
```

---

## 🎉 You're Done!

Your project is now on GitHub and ready to share with others!
