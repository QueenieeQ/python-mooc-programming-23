# Write your solution here
# Write your solution here
def shortest(my_list):
    # short_list = []
    print(my_list[0])
    short = my_list[0]
    for i in my_list:
        if len(i) < len(short):
            # short = i
            short = i
    return short
if __name__ == "__main__":
    my_list = ["Alan", "Susan", "Seymour", "Kim", "Susan"]

    result = shortest(my_list)
    print(result)