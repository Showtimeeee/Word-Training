import tkinter as tk
import tkinter.ttk as ttk
import random
import pyttsx3
import threading


class RandomWordApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Word App")
        self.master.geometry("600x220")
        self.master.configure(bg="#36253b")
        self.word_label = tk.Label(self.master, text="", font=("Comic Sans MS", 42), bg="#36253b")
        self.word_label.pack(pady=20)
        self.exit_label = tk.Label(self.master, text="Press Q to Exit", font=("Helvetica", 8))
        self.exit_label.place(relx=1.0, rely=0.9, anchor="ne")
        self.progress_bar = ttk.Progressbar(
            self.master, orient="horizontal", length=500, mode="determinate", maximum=10000)
        self.progress_bar.pack(pady=10)
        self.engine = pyttsx3.init()
        self.update_word()
        self.master.bind("<Key>", self.on_key_press)

    def rand_word(self):
        # read txt file
        with open("russian.txt", "r") as f:
            words = f.readlines()
        return random.choice(words).strip()

    def rand_color(self):
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        return random.choice(colors)

    def update_word(self):
        # rand value
        word = self.rand_word()
        color = self.rand_color()
        self.word_label.config(text=word, fg=color)
        threading.Thread(target=self.play_sound, args=(word,)).start()
        # progress bar
        self.progress_bar["value"] = 0
        self.progress_bar.start()
        self.update_progress(0)
        # the next update after 10 sec
        self.master.after(10100, self.update_word)

    def play_sound(self, word):
        # pyttsx3
        self.engine.say(word)
        self.engine.runAndWait()

    def update_progress(self, value):
        self.progress_bar["value"] = value
        if value < 10000:
            self.master.after(100, self.update_progress, value + 100)
        else:
            self.progress_bar.stop()
            self.progress_bar["value"] = 0

    def on_key_press(self, event):
        # press q to exit
        if event.char.lower() == 'q' or event.char.lower() == 'й':
            self.master.destroy()


root = tk.Tk()
app = RandomWordApp(root)
root.mainloop()
