# #Exercise1
# myList = [76, 92.3, "hello", True, 4, 76]
#
# myList.append("apple")
# myList.append(76)
# print(myList)
#
# myList.insert(3, "cat")
# print(myList)
#
# myList.insert(0, 99)
# print(myList)
#
# print(myList.index("hello"))
#
# print(myList.count(76))
#
# myList.remove(76)
# print(myList)
#
# myList.pop(myList.index(True))
# print(myList)


# #Exercise2
# def sum_of_squares(xs):
#     total = 0
#     for x in xs:
#         total += x * x
#     return total
#
# print(sum_of_squares([2, 3, 4]))


# #Exercise3
# def sum_evens(nums):
#     total = 0
#     for n in nums:
#         if n % 2 == 0:
#             total += n
#     return total
#
# print(sum_evens([1, 2, 3, 4, 5, 6]))


# #Exercise4
# def count_length(words):
#     count = 0
#     for w in words:
#         if len(w) == 5:
#             count += 1
#     return count
#
# print(count_length(["hello", "banana", "square", "apple", "java"]))


# #Exercise5
# def sum_until_even(nums):
#     total = 0
#     for n in nums:
#         if n % 2 == 0:
#             break
#         total += n
#     return total
#
# print(sum_until_even([1, 3, 5, 6, 7, 9]))


# #Exercise6
# def count_until_sam(words):
#     count = 0
#     for w in words:
#         count += 1
#         if w == "sam":
#             break
#     return count
#
# print(count_until_sam(["hi", "there", "sam", "how", "are", "you"]))


# #Exercise7
# def replace(s, old, new):
#     return new.join(s.split(old))
#
# def test(actual, expected):
#     if actual == expected:
#         print("Test passed.")
#     else:
#         print("Test failed.")
#
# test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')
#
# s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
# test(replace(s, 'om', 'am'),
#      'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')
#
# test(replace(s, 'o', 'a'),
#      'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')


#Exercise8
def find_max_val_in_list(num_list):
    max_val = num_list[0]
    for num in num_list:
        if num > max_val:
            max_val = num

    return max_val

print(find_max_val_in_list([1,2,3,4,5,6,7,8,9,10]))
print(find_max_val_in_list([-34, -35, -60, -5]))




