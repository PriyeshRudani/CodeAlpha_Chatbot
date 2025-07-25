import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class ModernChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeAlpha Chatbot")
        self.root.geometry("300x550")
        self.root.configure(bg="#121212")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TButton",
                             font=("Segoe UI", 10),
                             background="#00b894",
                             foreground="white",
                             padding=6)
        self.style.map("TButton",
                       background=[("active", "#019875")])

        self.style.configure("TEntry",
                             font=("Segoe UI", 12),
                             fieldbackground="#2d2d2d",
                             foreground="white",
                             padding=6)

        self.create_widgets()

    def create_widgets(self):
        self.chat_area = scrolledtext.ScrolledText(self.root,
                                                   wrap=tk.WORD,
                                                   font=("Segoe UI", 11),
                                                   bg="#1e1e1e",
                                                   fg="#ffffff",
                                                   state=tk.DISABLED)
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(self.root, bg="#121212")
        self.entry_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.entry = ttk.Entry(self.entry_frame)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", self.send_message)

        self.send_btn = ttk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_btn.pack(side=tk.RIGHT, padx=(5, 0))

        self.display_bot("Welcome! Type 'bye' to exit.")

    def display_user(self, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"You: {message}\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    def display_bot(self, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"Bot: {message}\n\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    def send_message(self, event=None):
        message = self.entry.get().strip()
        if not message:
            return
        self.display_user(message)
        self.entry.delete(0, tk.END)

        response = self.get_response(message.lower())
        self.display_bot(response)

        if message.lower() == "bye":
            self.entry.config(state=tk.DISABLED)
            self.send_btn.config(state=tk.DISABLED)

    def get_response(self, msg):
        if msg in ["hi", "hello"]:
            return "Hi there!"
        elif msg == "how are you":
            return "I'm good, thank you!"
        elif msg == "what's your name":
            return "I'm CodeBot, your assistant."
        elif msg == "bye":
            return "Goodbye! Have a great day."
        else:
            return "I didn't understand that. Please try something else."

if __name__ == "__main__":
    root = tk.Tk()
    ModernChatbot(root)
    root.mainloop()