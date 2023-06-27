list = []
index = 1
while True:
    print("The list is now", list)
    input2 = input("a(a)d, (r)emove or e(x)it:")
    # print(index)
    if input2 == "d":
        item = len(list)+1
        list.append(item)
    elif input2 == "r":
        list.pop(len(list)-1)
    elif input2 == "x":
        print("Bye!")
        break
    else:
        break
        


        

