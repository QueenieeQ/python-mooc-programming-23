def palindromes(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            return False
    return True

while True:
    user_input = input("Please type in a word (or 'exit' to quit): ")
    if user_input == "exit":
        break
    if palindromes(user_input):
        print(f"{user_input} is a palindrome!")
        break  # Stop the program if the input is a palindrome
    else:
        print("that wasn't a palindrome")

if __name__ == "__main__":
    palindromes