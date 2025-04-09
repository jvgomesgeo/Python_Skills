def char_count(word):
    new_word = ""
    d = {}
    for char in word:
        if char not in new_word:
            new_word += char
            d.update({char: word.count(char)})

    for key, value in d.items():
        print(f"Letter: {key}, Amount: {value}")


if __name__ == '__main__':
    user_input = input("Enter a string to get count: ")
    print(char_count(user_input))