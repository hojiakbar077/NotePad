import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("My Notepad")
        self.root.geometry("800x500")

        # Matn maydoni
        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=1, fill="both")

        # Menyu yaratish
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Fayl menyusi
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Yangi", command=self.new_file)
        self.file_menu.add_command(label="Ochish", command=self.open_file)
        self.file_menu.add_command(label="Saqlash", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Chiqish", command=self.root.quit)
        self.menu_bar.add_cascade(label="Fayl", menu=self.file_menu)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    Notepad(root)
    root.mainloop()
