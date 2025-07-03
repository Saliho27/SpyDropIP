from flask import Flask, request, redirect

app = Flask(__name__)

LOG_FILE = "ip_log.txt"
TARGET_URL = "https://example.com"  # غيّر هذا إلى الرابط الذي تريد إعادة التوجيه إليه

@app.route('/')
def log_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    with open(LOG_FILE, "a") as f:
        f.write(f"{ip}\n")
    return redirect(TARGET_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)