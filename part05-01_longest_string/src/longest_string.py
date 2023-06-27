# Write your solution here
def longest(strings: list):
    length_of_word = 0
    longest_word = ""
    # print(length_of_word)
    for item in strings:    
        # print(length_of_word)
        if len(item) > len(longest_word):
            # if longest_word == len(item):
            #     longest_word = longest_word
            # length_of_word = len(item)
            longest_word = item
    return longest_word
        

if __name__ == "__main__":
    strings = ['first', 'second', 'third']
    print(longest(strings))
