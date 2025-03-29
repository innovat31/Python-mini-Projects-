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


# 2nd program
import random

def get_random_activity():
    """Returns a random activity from the list."""
    activities = [
        "🎨 Paint or draw something creative",
        "📚 Read a new book or an article",
        "🧘 Practice meditation or yoga",
        "🎵 Listen to a new music album",
        "🍳 Try cooking a new recipe",
        "🏃 Go for a walk or jog",
        "🧩 Solve a puzzle or play a board game",
        "💡 Learn a new skill online",
        "🎬 Watch a documentary or a movie",
        "🎮 Play a video game",
        "🌿 Do some gardening or plant a new seed",
        "📖 Write in a journal or start a blog post",
        "🛠️ Try a DIY project",
        "☎️ Call or message a friend you haven't talked to in a while",
        "🌌 Stargaze or watch the sunset",
        "📝 Learn and practice a new language",
        "🎤 Sing karaoke or dance to your favorite song",
        "🧹 Clean and organize your room or workspace"
    ]
    
    return random.choice(activities)

# Main program loop
while True:
    print("\n🎲 Random Activity Generator 🎲")
    activity = get_random_activity()
    print(f"👉 Your activity: {activity}")
    
    repeat = input("\nDo you want another activity? (yes/no): ").lower()
    
    if repeat != "yes":
        print("Goodbye! 👋 Enjoy your activity!")
        break
