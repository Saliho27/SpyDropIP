from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

LOG_FILE = "ip_log.txt"
TARGET_URL = "https://example.com"  # ضع هنا الرابط الذي تريد إعادة التوجيه إليه

def log_ip(ip, user_agent):
    with open(LOG_FILE, "a") as f:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time} - IP: {ip} - User-Agent: {user_agent}\n")

@app.route('/')
def index():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    log_ip(ip, user_agent)
    return redirect(TARGET_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)