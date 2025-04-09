def prime_number(number):
    '''This function checks for prime number'''
    if number == 2:
        print("Its a prime number !")
    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                print(number, "Its not a prime number !")
            
            else:
                print(number, "Its a prime number")
                

 
if __name__ == '__main__':
    user_input = int(input("Enter a number: "))
    print(prime_number(user_input))
        