# 🚀 Quick Setup Guide

## Step-by-Step Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/JoseVenom/trackerbot.git
cd trackerbot
```

### 2️⃣ Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Get Your Credentials

#### Option A: Telegram Bot Token
1. Open Telegram and search for `@BotFather`
2. Send `/newbot`
3. Follow the steps
4. Copy the token

#### Option B: GitHub Personal Access Token
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Check: `repo` and `workflow`
4. Generate and copy token

### 5️⃣ Setup Environment
```bash
cp .env.example .env
```

Edit `.env`:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
GITHUB_TOKEN=your_github_token_here
GITHUB_REPO=JoseVenom/trackerbot
GITHUB_USERNAME=JoseVenom
FLASK_PORT=5000
```

### 6️⃣ Run the Bot
```bash
python bot.py
```

### 7️⃣ Run the API (Optional - in another terminal)
```bash
python app.py
```

## First Test

1. Open Telegram
2. Search for your bot (from step 4)
3. Send `/start`
4. Try adding a deposit:
   - Click "💰 Add Deposit"
   - Enter account name: `Bank Account 1`
   - Enter amount: `100`
   - Enter description: `Initial deposit`

5. Check GitHub - the data should be committed!

## Verify Everything Works

### Test Bot
- `/start` → Shows menu ✅
- Add transaction → Should show success ✅
- Check summary → Should show transaction ✅

### Test API
```bash
# In a new terminal
curl http://localhost:5000/api/deposits
curl http://localhost:5000/health
```

## Common Issues

| Issue | Solution |
|-------|----------|
| Bot not responding | Check TELEGRAM_BOT_TOKEN in .env |
| GitHub sync fails | Check GITHUB_TOKEN permissions |
| Port 5000 in use | Change FLASK_PORT in .env |
| Module not found | Run `pip install -r requirements.txt` |

## Next Steps

1. ✅ Bot is running
2. 📊 Add some transactions
3. 📈 Check the summaries
4. 🔗 Share GitHub links
5. 🌐 Use REST API for integrations

## Need Help?

- Check `/health` endpoint
- Review `.env` file
- Check bot token validity
- Verify GitHub token permissions

---

**You're all set! Happy tracking! 🎉**
