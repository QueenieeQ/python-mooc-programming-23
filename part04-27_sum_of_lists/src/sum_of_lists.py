# def list_sum(a, b):
#     result = []
#     for i,j in zip(a, b):
#         # for j in b:
#         sums = i + j
#         result.append(sums)
#     return result
def list_sum(list1: list, list2: list):
    results = []
    print((len(list1)))
    print(zip(list1, list2))
    for i in range(len(list1)):
        results.append(list1[i] + list2[i])
 
    return results

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))  # [8, 9, 10, 9, 10, 11, 10, 11, 12]
