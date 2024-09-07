import requests
from tkinter import Tk, Label, Button

def fetch_quote():
    base_url = "https://zenquotes.io/api/random"
    response = requests.get(base_url)
    if response.status_code == 200:
        quote_data = response.json()[0]
        quote = quote_data['q']
        author = quote_data['a']
        quote_label.config(text=f'"{quote}"\n\n- {author}')
    else:
        quote_label.config(text=f"Error: {response.status_code}")

# Set up the main window
root = Tk()
root.title("Quote Generator")

# Create and place the quote label
quote_label = Label(root, text="Click the button to get a quote", wraplength=400, justify="center", padx=20, pady=20)
quote_label.pack(pady=20)

# Create and place the button
fetch_button = Button(root, text="Fetch Quote", command=fetch_quote)
fetch_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
