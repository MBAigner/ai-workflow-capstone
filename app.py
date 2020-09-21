from flask import Flask, request, send_file
import model

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    pass


@app.route('/train', methods=['POST'])
def train():
    if not request.json or "country" not in request.json:
        return {"status": "error",
                "error_message": "country is required"}
    test = request.json["test"] if ("test" in request.json) else False
    country = request.json["country"]
    if country not in ['portugal', 'united_kingdom','hong_kong', 'eire',  'spain', 'france', 'singapore',
                        'all', 'norway', 'germany', 'netherlands']:
        return {"status": "error",
                "error_message": "country is not supported"}
    if country == "all":
        model.countries = ['portugal', 'united_kingdom','hong_kong', 'eire',  'spain', 'france', 'singapore',
                           'all', 'norway', 'germany', 'netherlands']
    else:
        model.countries = [country]

    try:
        print(model.countries)
        model.model_train(data_dir=model.TRAIN_PATH, test=test)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error",
                "error_message": str(e)}


@app.route('/logs', methods=['POST'])
def get_log():
    if not request.json or "type" not in request.json:
        return {"status": "error",
                "error_message": "no type requested (either 'predict' or 'train')"}
    log = request.json["type"]
    if log not in ["predict", "train"]:
        return {"status": "error",
                "error_message": "type should be either 'predict' or 'train')"}
    if log == "predict":
        path = "./logs/predict_log.csv"
    else:
        path = "./logs/train_log.csv"
    return send_file(
        path,
        as_attachment=True,
        attachment_filename="log.csv"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
