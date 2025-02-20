import cv2
import os

def test_images_in_clean_folder():
    input_folder = "images/clean"

    if not os.path.exists(input_folder):
        print(f"Папка не найдена: {input_folder}")
        return

    files = os.listdir(input_folder)
    if not files:
        print(f"Файлы в папке {input_folder} не найдены!")
        return

    print(f"Файлы, найденные в папке {input_folder}: {files}")

    for filename in files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            image_path = os.path.join(input_folder, filename)
            img = cv2.imread(image_path)
            if img is None:
                print(f"Ошибка чтения изображения: {image_path}")
            else:
                print(f"Изображение успешно прочитано: {image_path}")
        else:
            print(f"Файл {filename} не является изображением. Пропускаем.")

if __name__ == "__main__":
    test_images_in_clean_folder()
