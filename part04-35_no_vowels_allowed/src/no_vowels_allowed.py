# Write your solution here
def no_vowels(my_string):
    vowels = ["u","e","o","a","i"]
    result = ""
    # print(vowels)
    for item in my_string:
        if item not in vowels:
            result += item
    return result
            # print(my_string.replace(" ", item))
        


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))