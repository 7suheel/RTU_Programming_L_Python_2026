def analyze_sentence(text):
    characters = len(text)
    words = len(text.split())
    has_python = "python" in text.lower()

    return characters, words, has_python


if __name__ == "__main__":
    text = input("Enter a sentence: ")

    result = analyze_sentence(text)

    print("Characters:", result[0])
    print("Words:", result[1])
    print("Contains Python:", result[2])