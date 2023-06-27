# Write your solution here
# You can test your function by calling it within the following block
#  cần đo độ dài của hash, mỗi dòng cộng thêm 2 *, vd với 5 dòng cần 9*
def line(num, string):
    index = 1
    index2 = num - 1
    lines =1
    while lines <= num:
        hashes = (index * string)
        print(" "* index2 +hashes[0:index])
        index += 2
        index2 -= 1
        lines += 1
    print((num -1)*" "+"*")
def spruce(num):
        print("a spruce!")
        string = "*"
        line(num,string)
 
if __name__ == "__main__":
    spruce(3)
"""
def spruce(height):
    print("a spruce!")
    i = 1
    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i += 1
    print(" " * (height - 1) + "*")
"""