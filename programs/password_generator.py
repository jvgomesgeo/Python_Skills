import random
import string

def password_generator(len_password):

    numbers = list(string.digits)
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    special_chars = list(string.punctuation)


    random.shuffle(lowercase)
    random.shuffle(uppercase)
    random.shuffle(special_chars)
    random.shuffle(numbers)

    password = ''
    num = random.choice(numbers)


    password = ''
    for index in range(1, len_password +1):
        low_case = random.choice(lowercase)
        up_case = random.choice(uppercase)
        sp_char = random.choice(special_chars)

        chars_shuffled = [sp_char,num,low_case,up_case]

        char = chars_shuffled[(index -1) % 4]
        password += char
        
    return password

def main():
    while True:
        user_input = input("Enter the length of your password (min 4 chars): ")

        if not user_input.isdigit():
            print("Enter a number")
        
        else:
            user_input = int(user_input)
            break

    return print(password_generator(user_input))
        

if __name__ == '__main__':
    main()


