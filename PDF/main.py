from PIL import Image


def main():
    # Загружаем все изображения в отдельные переменные
    image1 = Image.open("Image_1.jpg")
    image2 = Image.open("Image_2.jpg")
    image3 = Image.open("Image_3.jpg")

    # Конвертируем все изображения в формат RGB
    image1.convert("RGB")
    image2.convert("RGB")
    image3.convert("RGB")

    # Создаем список изображений (без первого изображения)
    # При необходимости можно сохранить порядок изображений
    # Первое изображение "image1" не включается в этот список, так как оно будет использовано отдельно
    imageList = [image2, image3]

    # Создание PDF-файла
    fileName = "Cars.pdf"  # Имя PDF-файла
    # Используем первое изображение в качестве базового
    # PDF будет содержать изображения в следующем порядке:
    # image1, image2, image3, image4, image5
    # Первое изображение "image1" задает начальную страницу
    image1.save(fileName, save_all=True, append_images=imageList)

    # Конец программы
    print("Done")


if __name__ == "__main__":
    main()
