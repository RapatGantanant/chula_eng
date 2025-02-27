import tkinter as tk
import random

# List of Thai consonants with their names
THAI_CONSONANTS = [
    ("ก", "กอ ไก่ (Gor Gai)"),
    ("ข", "ขอ ไข่ (Khor Khai)"),
    ("ค", "คอ ควาย (Khor Khwai)"),
    ("ง", "งอ งู (Ngor Ngu)"),
    ("จ", "จอ จาน (Jor Jan)"),
    ("ฉ", "ฉอ ฉิ่ง (Chor Ching)"),
    ("ช", "ชอ ช้าง (Chor Chang)"),
    ("ซ", "ซอ โซ่ (Sor So)"),
    ("ญ", "ญอ หญิง (Yor Ying)"),
    ("ด", "ดอ เด็ก (Dor Dek)"),
    ("ต", "ตอ เต่า (Tor Tao)"),
    ("บ", "บอ ใบไม้ (Bor Bai Mai)"),
    ("ป", "ปอ ปลา (Por Pla)"),
    ("พ", "พอ พาน (Por Phan)"),
    ("ฟ", "ฟอ ฟัน (For Fun)"),
    ("ม", "มอ ม้า (Mor Ma)"),
    ("ร", "รอ เรือ (Ror Rua)"),
    ("ล", "ลอ ลิง (Lor Ling)"),
    ("ส", "สอ เสือ (Sor Suea)"),
    ("ห", "หอ หีบ (Hor Heep)")
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.card_front = True
        self.current_card = None
        
        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack(pady=20)
        
        self.text = self.canvas.create_text(200, 150, text="", font=("Arial", 40), fill="black")
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(pady=10)
        
        self.next_card()
        
    def next_card(self):
        self.current_card = random.choice(THAI_CONSONANTS)
        self.card_front = True
        self.canvas.itemconfig(self.text, text=self.current_card[0], font=("Arial", 80))
    
    def flip_card(self):
        if self.card_front:
            self.canvas.itemconfig(self.text, text=self.current_card[1], font=("Arial", 20))
        else:
            self.canvas.itemconfig(self.text, text=self.current_card[0], font=("Arial", 80))
        self.card_front = not self.card_front

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardGame(root)
    root.mainloop()