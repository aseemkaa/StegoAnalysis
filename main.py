import cv2

def main():
    image_path = "images/clean/bird-1232416_1280.png"

    img = cv2.imread(image_path)

    # Если img равен None, значит изображение не удалось загрузить
    if img is None:
        print("Ошибка чтения изображения. Проверьте путь и имя файла:", image_path)
    else:
        print("Изображение успешно загружено!")
        cv2.imshow("Loaded Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
