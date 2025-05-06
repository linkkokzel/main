import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

def get_dog_image():
    try:
        resp = requests.get("https://api.thedogapi.com/v1/images/search", timeout=10)
        resp.raise_for_status()
        img_url = resp.json()[0]['url']
        img_data = requests.get(img_url, timeout=10).content
        return img_data
    except Exception as e:
        messagebox.showerror("Ошибка", "Не удалось получить изображение собаки.")
        return None

def show_dog():
    img_data = get_dog_image()
    if img_data:
        img = Image.open(BytesIO(img_data))
        img.thumbnail((350, 350))
        tk_img = ImageTk.PhotoImage(img)
        image_label.config(image=tk_img)
        image_label.image = tk_img

def close_app_with_message():
    messagebox.showinfo("Внимание", "ты это не путай тут")
    root.destroy()

root = tk.Tk()
root.title("Dog API Развлекательное приложение")
root.geometry("700x700")
root.resizable(False, False)

title = tk.Label(root, text="Случайная собака (Dog API)", font=("Arial", 14))
title.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

btn_show = tk.Button(root, text="Показать собаку", command=show_dog, font=("Arial", 12), width=20)
btn_show.pack(pady=5)

btn_close = tk.Button(root, text="Не хочу смотреть на собак", command=close_app_with_message, font=("Arial", 12), width=20, fg="red")
btn_close.pack(pady=5)

root.mainloop()