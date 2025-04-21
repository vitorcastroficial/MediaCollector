from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/media")
def media():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL não fornecida"}), 400

    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        images = [img["src"] for img in soup.find_all("img", src=True)]
        videos = [video["src"] for video in soup.find_all("video", src=True)]
        audios = [audio["src"] for audio in soup.find_all("audio", src=True)]

        return jsonify({
            "images": images,
            "videos": videos,
            "audios": audios
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
