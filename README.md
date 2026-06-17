# 🏦 Bank Tracker Bot

A Telegram bot for tracking bank deposits and withdrawals with automatic cloud storage to GitHub and data visualization.

## Features

✨ **Core Features:**
- 💰 Add deposits to different accounts
- 💸 Add withdrawals from different accounts
- 📊 Daily deposit/withdrawal summaries
- 📈 Compare accounts across transactions
- ☁️ Automatic cloud storage (GitHub)
- 🔗 Generate shareable links for data
- 📱 Telegram bot interface
- 🌐 REST API with Flask

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- GitHub account with a personal access token
- Telegram bot token from BotFather

### 2. Clone the Repository
```bash
git clone https://github.com/JoseVenom/trackerbot.git
cd trackerbot
```

### 3. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
```bash
cp .env.example .env
```

Edit `.env` file with your credentials:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_REPO=JoseVenom/trackerbot
GITHUB_USERNAME=JoseVenom
FLASK_PORT=5000
```

### 6. Create Data Directory
```bash
mkdir -p data
```

### 7. Run the Telegram Bot
```bash
python bot.py
```

### 8. Run the Flask API (in another terminal)
```bash
python app.py
```

## Getting Credentials

### Telegram Bot Token
1. Open [BotFather](https://t.me/botfather) on Telegram
2. Type `/newbot`
3. Follow the instructions
4. Copy your bot token to `.env`

### GitHub Personal Access Token
1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `workflow`
4. Copy the token to `.env`

## Bot Commands

### Telegram Bot
- `/start` - Show main menu
- 💰 **Add Deposit** - Add a new deposit transaction
- 💸 **Add Withdrawal** - Add a new withdrawal transaction
- 📊 **Deposit Summary** - View today's deposit summary
- 📊 **Withdraw Summary** - View today's withdrawal summary
- 🔗 **Deposit Links** - Get GitHub links for deposit data
- 🔗 **Withdraw Links** - Get GitHub links for withdrawal data
- 📈 **Compare Accounts** - Compare all accounts

### REST API Endpoints

#### Get Deposits
```bash
GET /api/deposits
```
Response: Total deposits summary with breakdown by account

#### Get Withdrawals
```bash
GET /api/withdrawals
```
Response: Total withdrawals summary with breakdown by account

#### Daily Summary
```bash
GET /api/daily-summary?date=2024-01-15
```
Response: Daily summaries for deposits and withdrawals

#### Compare Accounts
```bash
GET /api/compare
```
Response: Account comparison with totals, counts, and averages

#### Get Shareable Links
```bash
GET /api/links
```
Response: GitHub links for both deposits and withdrawals data

#### Export Data
```bash
GET /api/export?type=all  # all, deposits, or withdrawals
```
Response: JSON export of transaction data

#### Health Check
```bash
GET /health
```
Response: API health status

## Data Storage

All data is automatically saved to:
- `data/deposits.csv` - All deposit transactions
- `data/withdrawals.csv` - All withdrawal transactions

These files are synced to GitHub for cloud backup and sharing.

## CSV File Structure

Both CSV files contain:
- **Date**: Transaction date (YYYY-MM-DD)
- **Account**: Account name
- **Amount**: Transaction amount
- **Description**: Transaction notes
- **Timestamp**: Full timestamp (YYYY-MM-DD HH:MM:SS)

## Features Explained

### Daily Summary
Shows total deposits/withdrawals for today with breakdown by account.

### Account Comparison
Compares all accounts showing:
- Total amount per account
- Number of transactions
- Average transaction amount

### Cloud Storage
All transactions are automatically:
1. Saved locally as CSV
2. Synced to GitHub for backup
3. Accessible via shareable GitHub links

### Shareable Links
Two types of links are generated:
- **GitHub Link**: View formatted file on GitHub
- **Raw Data Link**: Direct CSV data access

## Project Structure
```
trackerbot/
├── bot.py                 # Telegram bot implementation
├── app.py                 # Flask API
├── config.py              # Configuration management
├── csv_manager.py         # CSV file operations
├── github_manager.py      # GitHub integration
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── data/                 # Transaction data (auto-created)
│   ├── deposits.csv
│   └── withdrawals.csv
└── README.md             # This file
```

## Troubleshooting

### Bot not responding
- Check if `TELEGRAM_BOT_TOKEN` is correct
- Ensure bot is running: `python bot.py`
- Check internet connection

### GitHub sync issues
- Verify `GITHUB_TOKEN` has `repo` and `workflow` permissions
- Check `GITHUB_REPO` format: `owner/repo`
- Ensure token hasn't expired

### Data not saving
- Check if `data/` directory exists
- Verify write permissions in the directory
- Check disk space

## Security Notes
- Never commit `.env` file with real credentials
- Use GitHub personal access tokens with minimal required scopes
- Keep credentials secure and rotate regularly
- Use environment variables for all sensitive data

## Future Enhancements
- 📱 Web dashboard for data visualization
- 📈 Monthly/yearly reports
- 🔔 Transaction alerts
- 📧 Email notifications
- 🔐 User authentication
- 💾 Database integration

## Contributing
Feel free to submit issues and pull requests!

## License
MIT License

## Support
For issues or questions, please create an issue on the GitHub repository.

---

**Made with ❤️ by JoseVenom**
