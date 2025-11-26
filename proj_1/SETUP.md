# 🔧 Setup Instructions

## 1. Copy API Keys
```bash
cp config/api_keys_template.py config/api_keys.py
```

## 2. Edit config/api_keys.py with your real keys:
```python
AWS_ACCESS_KEY_ID = 'YOUR_ACTUAL_AWS_KEY'
AWS_SECRET_ACCESS_KEY = 'YOUR_ACTUAL_AWS_SECRET'
BEDROCK_API_KEY = "YOUR_ACTUAL_BEDROCK_KEY"
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 4. Test Setup
```bash
python examples/basic_chat.py
```

⚠️ **Never commit api_keys.py to Git!**