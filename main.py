from flask import Flask, request
import os

app = Flask(__name__)

# Intentionally simple route for demonstration
@app.route("/")
def home():
    return "Hello, DevSecOps Beginner!"

# A deliberately risky code pattern to show how SAST (Bandit) catches it
@app.route("/debug")
def debug_mode():
    # Bandit will flag this because running code from user input is dangerous
    cmd = request.args.get('cmd', 'echo safe')
    os.system(cmd)
    return "Executed debug check."

if __name__ == "__main__":
    app.run(debug=True, port=5000)