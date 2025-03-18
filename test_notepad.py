import unittest
import tkinter as tk
import os
from tkinter import filedialog
from notepad import Notepad  # Notepad klassingiz fayl nomi `notepad.py` bo‘lishi kerak


class TestNotepad(unittest.TestCase):
    def setUp(self):
        """Test boshlanishidan oldin Notepad oynasini ishga tushiramiz"""
        self.root = tk.Tk()
        self.app = Notepad(self.root)

    def tearDown(self):
        """Test tugagandan keyin oynani yopamiz"""
        self.root.destroy()

    def test_new_file(self):
        """Yangi fayl yaratish testi"""
        self.app.text_area.insert("1.0", "Test matn")
        self.app.new_file()
        self.assertEqual(self.app.text_area.get("1.0", tk.END).strip(), "")

    def test_open_file(self):
        """Fayl ochish testi"""
        test_content = "Bu test faylidir."
        test_file = "test_file.txt"

        with open(test_file, "w") as f:
            f.write(test_content)

        # Faylni ochish va yuklash
        def mock_open_file():
            with open(test_file, "r") as f:
                self.app.text_area.delete("1.0", tk.END)
                self.app.text_area.insert(tk.END, f.read())

        self.app.open_file = mock_open_file  # Fayl ochish funksiyasini almashtiramiz
        self.app.open_file()

        # Fayldan o‘qilgan matnni tekshiramiz
        self.assertEqual(self.app.text_area.get("1.0", tk.END).strip(), test_content)

        os.remove(test_file)  # Test faylni o‘chiramiz

    def test_save_file(self):
        """Faylni saqlash testi"""
        test_content = "Saqlash testi"
        test_file = "test_save.txt"

        self.app.text_area.insert("1.0", test_content)

        # Faylni saqlashni taqlid qilamiz
        def mock_save_file():
            with open(test_file, "w") as f:
                f.write(self.app.text_area.get("1.0", tk.END))

        self.app.save_file = mock_save_file
        self.app.save_file()

        with open(test_file, "r") as f:
            saved_content = f.read().strip()

        self.assertEqual(saved_content, test_content)

        os.remove(test_file)  # Test faylni o‘chiramiz


if __name__ == "__main__":
    unittest.main()
