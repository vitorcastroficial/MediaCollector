from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return "API de Coleta de Mídia Online!"

@app.route("/media")
def media():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL não fornecida"}), 400

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        images = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]
        videos = [video['src'] for video in soup.find_all('video') if 'src' in video.attrs]
        audios = [audio['src'] for audio in soup.find_all('audio') if 'src' in audio.attrs]

        return jsonify({
            "images": images,
            "videos": videos,
            "audios": audios
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
