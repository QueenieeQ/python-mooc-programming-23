# Write your solution here
def length_of_longest(my_list):
    best = ""
    for (i) in my_list:
        # print(len(i))
        if len(i) > len(best):
            best = i
    return len(best)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
