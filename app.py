from flask import Flask, render_template, request, jsonify, send_file
import json
from csv_manager import CSVManager
from github_manager import GitHubManager
from config import Config
from datetime import datetime
import io

app = Flask(__name__)
csv_manager = CSVManager()
github_manager = GitHubManager()

@app.route('/', methods=['GET'])
def index():
    """Main dashboard"""
    deposits_summary = csv_manager.get_total_summary('deposits')
    withdrawals_summary = csv_manager.get_total_summary('withdrawals')
    
    return jsonify({
        'status': 'success',
        'data': {
            'deposits': deposits_summary,
            'withdrawals': withdrawals_summary
        }
    })

@app.route('/api/deposits', methods=['GET'])
def get_deposits():
    """Get all deposits"""
    summary = csv_manager.get_total_summary('deposits')
    return jsonify(summary)

@app.route('/api/withdrawals', methods=['GET'])
def get_withdrawals():
    """Get all withdrawals"""
    summary = csv_manager.get_total_summary('withdrawals')
    return jsonify(summary)

@app.route('/api/daily-summary', methods=['GET'])
def get_daily_summary():
    """Get daily summary for both deposits and withdrawals"""
    date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
    
    deposits = csv_manager.get_daily_summary('deposits', date)
    withdrawals = csv_manager.get_daily_summary('withdrawals', date)
    
    return jsonify({
        'date': date,
        'deposits': deposits,
        'withdrawals': withdrawals
    })

@app.route('/api/compare', methods=['GET'])
def compare_accounts():
    """Compare accounts across deposits and withdrawals"""
    deposits_compare = csv_manager.compare_accounts('deposits')
    withdrawals_compare = csv_manager.compare_accounts('withdrawals')
    
    return jsonify({
        'deposits': deposits_compare,
        'withdrawals': withdrawals_compare
    })

@app.route('/api/links', methods=['GET'])
def get_links():
    """Get shareable GitHub links"""
    return jsonify({
        'deposits': {
            'github': github_manager.get_file_url('data/deposits.csv'),
            'raw': github_manager.get_raw_file_url('data/deposits.csv')
        },
        'withdrawals': {
            'github': github_manager.get_file_url('data/withdrawals.csv'),
            'raw': github_manager.get_raw_file_url('data/withdrawals.csv')
        }
    })

@app.route('/api/export', methods=['GET'])
def export_data():
    """Export data as JSON"""
    export_type = request.args.get('type', 'all')  # deposits, withdrawals, or all
    
    data = {}
    
    if export_type in ['deposits', 'all']:
        data['deposits'] = csv_manager.get_total_summary('deposits')
    
    if export_type in ['withdrawals', 'all']:
        data['withdrawals'] = csv_manager.get_total_summary('withdrawals')
    
    return jsonify(data)

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, port=Config.FLASK_PORT)
