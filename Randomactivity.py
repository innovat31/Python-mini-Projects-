import random

def suggest_activity():
    activities = [
        "Go for a walk in the park 🌳",
        "Read a new book 📖",
        "Try cooking a new recipe 🍳",
        "Watch a documentary 🎥",
        "Do a quick workout 🏋️",
        "Start a journal 📝",
        "Listen to a podcast 🎧",
        "Learn a new skill or hobby 🎨",
        "Call a friend or family member ☎️",
        "Meditate for 10 minutes 🧘",
        "Solve a puzzle 🧩",
        "Go stargazing ✨",
        "Write a short story or poem ✍️",
        "Explore a new place in your city 🌆"
    ]
    
    return random.choice(activities)

if __name__ == "__main__":
    print("Here's a random activity for you to try:")
    print(suggest_activity())
