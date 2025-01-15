def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        word_count = count_words(file_contents)
        print(f"Number of words: {word_count}")

        character_counts = count_characters(file_contents)
        print("Character counts:")
        for char, count in character_counts.items():
            print(f"{char}: {count}")

        generate_report(word_count, character_counts )

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower() #converts to lowercase
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def generate_report(word_count, character_counts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    sorted_chars = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        print(f"the '{char}' character was found {count} times")


    print("---end report---")
main()
