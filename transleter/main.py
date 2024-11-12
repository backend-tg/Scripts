from translate import Translator
from tkinter import *
from tkinter import ttk

root = Tk()
rBtn = IntVar()
root.title("Переводчик")
root.geometry("730x480")
root.resizable(width=False, height=False)


def translater():
    txt = pole.get("1.0", END).strip()  # Получаем текст для перевода
    if rBtn.get() == 0:
        translator = Translator(from_lang="English", to_lang="Russian")
    elif rBtn.get() == 1:
        translator = Translator(from_lang="Russian", to_lang="English")
    w = translator.translate(txt)  # Переводим текст
    poleTranslate.delete("1.0", END)  # Очищаем поле для результата
    poleTranslate.insert("1.0", w)  # Вставляем переведенный текст


pole = Text(root, width=80, height=10, font="Arial, 13")
pole.pack(pady=10)

algo01 = Radiobutton(
    root, text="Перевод на русский", variable=rBtn, value=0, font="Arial, 12"
)
algo01.place(x=50, y=215)

Btn = ttk.Button(root, text="Перевести", command=translater)
Btn.pack()

algo02 = Radiobutton(
    root, text="Перевод на английский", variable=rBtn, value=1, font="Arial, 12"
)
algo02.place(x=430, y=215)

poleTranslate = Text(root, width=80, height=10, font="Arial, 13")
poleTranslate.pack(pady=10)

root.mainloop()
