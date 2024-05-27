#Task 1:


def mood_response(mood):
    mood = mood.lower()  # Convert the mood to lowercase to handle case insensitivity
    responses = {
        "happy": "That's great to hear! Keep smiling!",
        "sad": "I'm sorry to hear that. I hope things get better soon.",
        "excited": "Wow, that's exciting! Enjoy the moment!",
        "angry": "Take a deep breath. It's important to stay calm.",
        "tired": "Get some rest. It's important to take care of yourself.",
    }
    return responses.get(mood, "I don't have a response for that mood. Can you tell me more?")

def main():
    mood = input("How are you feeling today? ")
    print(mood_response(mood))

if __name__ == "__main__":
    main()
