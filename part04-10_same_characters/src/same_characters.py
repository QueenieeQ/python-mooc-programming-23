
def same_chars(string, index1, index2):
    if index1 >= 0 and index1 < len(string) and index2 >= 0 and index2 < len(string):

        return string[index1] == string[index2]
    else:
        return False

if __name__ == "__main__":
    print(same_chars("coder", 1, 10))
    # print(same_chars)