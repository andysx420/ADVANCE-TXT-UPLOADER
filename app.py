from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'AndySX bot is running! ✅'

if __name__ == "__main__":
    # Heroku uses dynamic port allocation via $PORT environment variable
    port = int(os.environ.get("PORT", 5000))  # default to 5000 for local dev
    app.run(host='0.0.0.0', port=port)
