from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['POST'])
def run_script():
    subprocess.run(["python", "main.py"])
    return jsonify({"status": "Script executado com sucesso!"})

@app.route('/stop-script', methods=['POST'])
def stop_script():
    return jsonify({"status": "Conversation ended successfully"})

if __name__ == '__main__':
    app.run(debug=True)
