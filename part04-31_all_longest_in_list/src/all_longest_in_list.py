def all_the_longest(my_list):
    longest = []
    long1 = my_list[0]
    for i in my_list:
        if len(i) > len(long1):
            long1 = i
            longest = [i]
        elif len(i) == len(long1):
            longest.append(i)
    return longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)  # Output: ['eleventh']
