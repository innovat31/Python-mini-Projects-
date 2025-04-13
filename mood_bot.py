# mood_bot.py

print("Hi, I'm MoodBot 🤖. How are you feeling today?")

mood = input("Enter your mood (happy, sad, angry, bored): ").lower()

if mood == "happy":
    print("That's awesome! Keep smiling and spread the joy 😊")
elif mood == "sad":
    print("I'm here for you. Remember, it's okay to feel down sometimes 💙")
elif mood == "angry":
    print("Take a deep breath... Try to relax and stay calm 🧘")
elif mood == "bored":
    print("Maybe try reading a book, watching a movie, or learning Python! 📚")
else:
    print("Hmm... I’m not sure how to respond to that, but I hope you’re okay! 🤔")
