from flask import Flask, request
import requests

app = Flask(__name__)

# ضع هنا توكن بوت Telegram الخاص بك
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# ضع هنا رقم الـ Chat ID الخاص بك
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Failed to send message: {e}")

@app.route('/')
def log_ip():
    # الحصول على IP الزائر
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # رسالة ترسل إلى Telegram
    message = f"🆕 زائر جديد!\nIP: <b>{ip}</b>"

    # إرسال الرسالة
    send_telegram_message(message)

    # إظهار رسالة تأكيد للزائر
    return "<h2>تم تسجيل زيارتك بنجاح ✅</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
