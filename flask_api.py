from flask import Flask, jsonify, request
from core import get_paraphrases

app = Flask(__name__)


@app.route("/paraphrase", methods=["GET"])
def get_paraphrase():
    args = request.args
    tree = args.get(key="tree", type=str)
    limit = args.get(key="limit", default=20, type=int)
    return jsonify(get_paraphrases(tree, limit))


if __name__ == "__main__":
    app.run(debug=True)
