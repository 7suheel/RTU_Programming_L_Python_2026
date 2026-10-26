def count_characters(text):
    count = 0

    for char in text:
        if not char.isspace():
            count += 1

    return count


def count_words(text):
    return len(text.split())


def extract_numbers(text):
    numbers = []

    for word in text.split():
        word = word.rstrip(".,!?;:")

        if word.isdigit():
            numbers.append(int(word))
        elif word.startswith("-") and word[1:].isdigit():
            numbers.append(int(word))

    return numbers


def analyze_text(text):
    characters = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)

    total = sum(numbers)

    if len(numbers) > 0:
        average = total / len(numbers)
    else:
        average = 0

    return {
        "characters": characters,
        "words": words,
        "numbers": numbers,
        "sum": total,
        "average": average,
    }


if __name__ == "__main__":
    text = input("Enter text: ")
    result = analyze_text(text)

    print("Characters:", result["characters"])
    print("Words:", result["words"])
    print("Numbers:", result["numbers"])
    print("Sum:", result["sum"])
    print("Average:", format(result["average"], ".2f"))
