# Write your solution here
def anagrams(text1, text2):
    # print(sorted(text1))
    # print(sorted(text2))
    if sorted(text1) == sorted(text2):
        return True
    else:
        return False
if __name__ == "__main__":
    text1 = "love"
    text2 = "ovle"
    print(anagrams(text1, text2))