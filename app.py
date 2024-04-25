from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Statik dosya dizini ayarı
app.static_folder = 'static'
# Statik URL ayarı
app.static_url_path = '/static'

# Ana sayfa
@app.route('/')
def index():
    return 'Hoş geldiniz! Fotoğraf yükleme için /upload sayfasına gidin.'

# Fotoğraf yükleme endpoint'i
@app.route('/upload', methods=['POST'])
def upload_photo():
    if 'photo' in request.files:
        photo = request.files['photo']
        photo.save(os.path.join(app.static_folder, 'uploaded_photo.jpg'))  # Yüklenen fotoğrafı static dizinine kaydet
        photo_url = f"{request.host_url}static/uploaded_photo.jpg"  # Yüklenen fotoğrafın URL'si
        return jsonify({'message': 'Fotoğraf başarıyla yüklendi.', 'photo_url': photo_url})
    else:
        return jsonify({'error': 'Hata: Fotoğraf yüklenemedi.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
