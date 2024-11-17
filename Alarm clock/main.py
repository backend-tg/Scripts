from tkinter import *
from tkinter import messagebox
import datetime
import threading
import time
import winsound


stop_alarm = False  # Глобальная переменная для остановки будильника


def validate_time(hour, minute, second):
    """Проверка корректности введённого времени."""
    try:
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        if 0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60:
            return True
        else:
            return False
    except ValueError:
        return False


def actual_time():
    """Обработчик нажатия кнопки установки будильника."""
    global stop_alarm
    stop_alarm = False  # Сброс состояния будильника
    h = hour.get()
    m = min.get()
    s = sec.get()

    if validate_time(h, m, s):
        set_alarm_timer = f"{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)}"
        threading.Thread(target=alarm, args=(set_alarm_timer,), daemon=True).start()
        messagebox.showinfo("Будильник установлен", f"Будильник установлен на {set_alarm_timer}")
    else:
        messagebox.showerror("Ошибка", "Введите корректное время в формате ЧЧ:ММ:СС!")


def alarm(set_alarm_timer):
    """Логика работы будильника."""
    global stop_alarm
    while not stop_alarm:
        time.sleep(1)  # Ожидание 1 секунды
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_timer and not stop_alarm:
            print("Время просыпаться!")
            messagebox.showinfo("Будильник", "Время просыпаться!")
            winsound.PlaySound("sound.mp3", winsound.SND_ASYNC)
            break


def stop_alarm_action():
    """Функция для остановки будильника."""
    global stop_alarm
    stop_alarm = True
    messagebox.showinfo("Будильник", "Будильник остановлен.")


# Создание интерфейса
clock = Tk()
clock.title("Будильник")
clock.geometry("400x300")
clock.resizable(False, False)

# Заголовки и инструкции
Label(
    clock,
    text="Введите время в 24-часовом формате",
    fg="white",
    bg="black",
    font=("Arial", 12),
    pady=10,
).pack(fill="x")
Label(clock, text="Часы  Минуты  Секунды", font=("Arial", 10)).pack(pady=5)

# Поля ввода времени
frame = Frame(clock)
frame.pack(pady=10)

hour = StringVar()
min = StringVar()
sec = StringVar()

Entry(frame, textvariable=hour, width=5, font=("Arial", 14), justify="center").grid(row=0, column=0, padx=5)
Entry(frame, textvariable=min, width=5, font=("Arial", 14), justify="center").grid(row=0, column=1, padx=5)
Entry(frame, textvariable=sec, width=5, font=("Arial", 14), justify="center").grid(row=0, column=2, padx=5)

# Кнопка для установки будильника
Button(
    clock,
    text="Установить будильник",
    command=actual_time,
    fg="white",
    bg="green",
    font=("Arial", 12),
    width=20,
).pack(pady=10)

# Кнопка для остановки будильника
Button(
    clock,
    text="Остановить будильник",
    command=stop_alarm_action,
    fg="white",
    bg="red",
    font=("Arial", 12),
    width=20,
).pack(pady=10)

# Запуск интерфейса
clock.mainloop()
