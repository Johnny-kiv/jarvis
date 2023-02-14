import cv2
import face_recognition

# Включаем первую камеру
cap = cv2.VideoCapture(0)

# "Прогреваем" камеру, чтобы снимок не был тёмным
for i in range(30):
    cap.read()

# Делаем снимок
ret, frame = cap.read()

# Записываем в файл
cv2.imwrite('imgs/img2.png', frame)

# Отключаем камеру
cap.release()
def compare_faces(img_path):
    ves = face_recognition.load_image_file("imgs/ves.png")
    ves_encoding = face_recognition.face_encodings(ves)[0]
    img = face_recognition.load_image_file(img_path)
    img_encoding = face_recognition.face_encodings(img)[0]
    result = face_recognition.compare_faces([ves_encoding],img_encoding)
#    print(result)
    if result == [True]:
        return "Добро пожаловать"
    else:
        return "Это кто?"

def main():
   # face_rec()
   print(compare_faces(img_path="imgs/img2.png"))
if __name__ == '__main__':
    main()