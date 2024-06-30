
print("Loading ...")

import tkinter as tk
from tkinter import messagebox
from model import *

device = "cuda:0" if torch.cuda.is_available() else "cpu"
tokenizer, model = get_fine_tuned_model("fine_tuned_model", device = device)

bg_color = "#0099AA"


# Function to analyze the sentiment (for demo purposes, it randomly decides positive or negative)
def analyze_sentiment():
    sentence = text_box.get("1.0", tk.END).strip()
    
    # Placeholder logic for sentiment analysis
    # Replace this with actual sentiment analysis logic
    if not sentence:
        messagebox.showwarning("Input Error", "Please enter some text.")
        result_label.config(text = "")
        return
    tokens = tokenizer(sentence, padding="max_length", truncation=True, return_tensors="pt").to(device)
    
    logits = model(**tokens).logits
    pred = torch.argmax(logits, dim = -1)
    percent = torch.max(torch.nn.functional.softmax(logits))
    sentiment = "POSITIVE" if pred == 1 else "NEGATIVE"
    result_label.config(text=f"{sentiment} : {percent*100:.1f}%", fg="green" if sentiment == "POSITIVE" else "red")

# Create the main window
root = tk.Tk()
root.title("Sentiment Analyzer")
root.geometry("600x500")
root.configure(bg=bg_color)

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter text to analyze sentiment:", bg=bg_color, fg="white", font=("Arial", 22))
instruction_label.pack(pady=10)

# Create a text box for user input
text_box = tk.Text(root, height=10, width=50, font=("Arial", 12), wrap='word', padx=15, pady = 15)
text_box.pack(pady = 15)

# Create an Analyze button
analyze_button = tk.Button(root, text="Analyze", command=analyze_sentiment, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
analyze_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", bg=bg_color, font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()