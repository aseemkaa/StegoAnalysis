import cv2
import os

def embed_message(image_path, message, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Ошибка чтения изображения: {image_path}")
        return

    binary_message = ''.join(format(ord(ch), '08b') for ch in message)
    message_length = len(binary_message)

    flat_img = img.flatten()

    if message_length > len(flat_img):
        print(f"Сообщение слишком длинное для изображения: {image_path}")
        return

    for i in range(message_length):
        flat_img[i] = (flat_img[i] & 254) | int(binary_message[i])

    stego_img = flat_img.reshape(img.shape)
    cv2.imwrite(output_path, stego_img)
    print(f"Stego-изображение сохранено: {output_path}")

def process_images(input_folder, output_folder, message):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            embed_message(image_path, message, output_path)

if __name__ == "__main__":
    input_folder = "images/clean"
    output_folder = "images/stego"
    message = "Асем"
    process_images(input_folder, output_folder, message)
