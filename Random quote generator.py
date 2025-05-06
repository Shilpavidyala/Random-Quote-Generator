import random

quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "You miss 100% of the shots you don’t take.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The future depends on what you do today."
]

def show_quote():
    print("💡 Random Quote of the Day:")
    print(random.choice(quotes))

if __name__ == "__main__":
    show_quote()
