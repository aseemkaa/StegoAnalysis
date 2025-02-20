import cv2
import os
import matplotlib.pyplot as plt

def analyze_lsb(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Ошибка чтения изображения:", image_path)
        return None
    # Извлекаем младший бит каждого пикселя
    lsb = img & 1
    ratio = lsb.sum() / lsb.size
    return ratio

def collect_metrics(folder):
    metrics = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            image_path = os.path.join(folder, filename)
            ratio = analyze_lsb(image_path)
            if ratio is not None:
                metrics.append(ratio)
    return metrics

def main():
    clean_folder = "images/clean"
    stego_folder = "images/stego"

    clean_metrics = collect_metrics(clean_folder)
    stego_metrics = collect_metrics(stego_folder)

    print("Метрики для чистых изображений:", clean_metrics)
    print("Метрики для stego-изображений:", stego_metrics)

    plt.hist(clean_metrics, bins=10, alpha=0.5, label="Чистые изображения")
    plt.hist(stego_metrics, bins=10, alpha=0.5, label="Stego-изображения")
    plt.xlabel("Отношение единиц в LSB")
    plt.ylabel("Количество изображений")
    plt.title("Распределение LSB-метрики")
    plt.legend(loc="upper right")
    plt.show()

if __name__ == "__main__":
    main()
