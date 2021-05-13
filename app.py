from flask import Flask, request, jsonify
from date import alchemy
from models import show

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlit://data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'supersecreto'

@app.before_first_request
def creat_tabe():
    alchemy.create_all()

@app.route('/', methods=['GET'])
def home():
    return 'Olá Mundo!', 200

@app.route('/show', methods=['POST'])
def creat_show():
    request_data = request.get_json()
    new_show = show.ShowModel(request_data['name'])
    new_show.saveDB()
    result = show.ShowModel.find_by_id(new_show.id)
    return jsonify(result.json())

if __name__ == '__main__':
    from date import alchemy
    alchemy.init_app(app)
    app.run(port=5000, debug=True)