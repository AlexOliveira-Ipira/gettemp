from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Olá Mundo!', 200

app.run(port=5000, debug=True)