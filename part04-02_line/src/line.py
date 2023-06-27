# Write your solution here
# You can test your function by calling it within the following block
def line(line,string):
    if string == "":
        print("*"*line)
    else:
        print(string[0]*line)
if __name__ == "__main__":
    # line(5, "x")
    line(7, "")
    line(5, "xxx")