from flask import Flask, render_template, request, jsonify
from main import AsiaonPlateBot
import os

app = Flask(__name__)
bot = AsiaonPlateBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.json.get('message', '')
        if not message.strip():
            return jsonify({'error': 'Empty message'})
        
        response = bot.process_query(message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': f'Sorry, I encountered an error: {str(e)}'})

@app.route('/reset', methods=['POST'])
def reset():
    global bot
    bot = AsiaonPlateBot()
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)