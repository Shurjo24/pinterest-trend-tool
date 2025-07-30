from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Your Pinterest Trend Tool is working on Render!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
