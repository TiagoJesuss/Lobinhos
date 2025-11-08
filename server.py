from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['POST'])
def run_script():
    # Executa o script Python
    subprocess.run(["python", "main.py"])
    return jsonify({"status": "Script executado com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
