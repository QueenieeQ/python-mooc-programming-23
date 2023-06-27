def most_common_character(mu_string :str):
    most_common = mu_string[0]
    # print(string[0])
    for item in mu_string:
        if mu_string.count(item) > mu_string.count(most_common):
            most_common = item
            # print(most_common[0])
    return most_common

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
