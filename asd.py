import cv2
import requests

def take_photo():
    # Kamera yakalamayı başlat
    cap = cv2.VideoCapture(0)

    # Kamera açık olduğu sürece devam et
    ret, frame = cap.read()
    if not ret:
        print("Kamera açılamadı.")
        return

    # Kareyi kaydet
    cv2.imwrite('captured_photo.jpg', frame)

    # Kamerayı serbest bırak
    cap.release()
    cv2.destroyAllWindows()

def upload_photo():
    # Yüklenecek fotoğraf dosyasının adı
    filename = 'captured_photo.jpg'

    # Yüklenecek web sitesinin URL'si
    upload_url = 'http://127.0.0.1:5000/upload'  # Flask uygulamasının çalıştığı URL'yi buraya ekleyin

    # Fotoğraf dosyasını açıp yükleme isteği yap
    with open(filename, 'rb') as file:
        files = {'photo': (filename, file)}
        response = requests.post(upload_url, files=files)

    # Yükleme işlemi başarılıysa URL'yi döndür, aksi halde hata mesajını döndür
    if response.status_code == 200:
        return response.text
    else:
        return f'Hata: {response.status_code} - {response.reason}'

if __name__ == "__main__":
    take_photo()
    photo_url = upload_photo()
    print("Çekilen fotoğrafın URL'si:", photo_url)
