from flask import Flask

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    pass


@app.route('/train', methods=['POST'])
def train():
    pass


@app.route('/logs', methods=['POST'])
def get_logs():
    pass
