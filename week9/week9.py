# #Exercise1
# def is_odd(n):
#     return n % 2 != 0
#
# print(is_odd(3))
# print(is_odd(4))
# print(is_odd(-7))


# #Exercise2
# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#     return False
#
# print(is_leap_year(2024))
# print(is_leap_year(1900))
# print(is_leap_year(2000))


# #Exercise3
# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n + 1):
#         total = total + i
#         print(i, "\t", total)
#
# print_triangular_numbers(5)


# #Exercise4
# def is_prime(n):
#     if n < 2:
#         return False
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True
#
# print(is_prime(2))
# print(is_prime(17))
# print(is_prime(1))
# print(is_prime(21))


# #Exercise5
# def reverse(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result
#
# print(reverse("hello"))
# print(reverse("Python"))
# print(reverse(""))


# #Exercise6
# def remove_all(substr, s):
#     if substr == "":
#         return s
#     result = ""
#     i = 0
#     while i < len(s):
#         if s[i:i + len(substr)] == substr:
#             i = i + len(substr)
#         else:
#             result = result + s[i]
#             i = i + 1
#     return result
#
# print(remove_all("an", "banana"))
# print(remove_all("cyc", "bicycle"))
# print(remove_all("iss", "Mississippi"))


# #Exercise7
# def encrypt(message, key):
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     key = key.upper()
#     result = ""
#     for ch in message:
#         upper_ch = ch.upper()
#         if upper_ch in alphabet:
#             index = alphabet.index(upper_ch)
#             new_ch = key[index]
#             if ch.islower():
#                 new_ch = new_ch.lower()
#             result = result + new_ch
#         else:
#             result = result + ch
#     return result
#
# key = "QTGWERYUIOPASDFHJKLZXCVBNM"
# print(encrypt("ABC", key))
# print(encrypt("Hello World!", key))


#Exercise8
def remove_dups(s):
    result = ""
    for ch in s:
        if ch.lower() not in result.lower():
            result = result + ch
    return result

print(remove_dups("hello world"))



