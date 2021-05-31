import random
import os
# --------------------------------------
# random.seed(10)
# print(random.random())
# ----------------------
# print(random.random())
#capture the state:
# state = random.getstate()
#print another random number:
# print(random.random())
#restore the state:
# random.setstate(state)
#and the next random number should be the same as when you captured the state:
# print(random.random())
# ---------------------------------------------
# Return an 8 bits sized integer
# print(random.getrandbits(8))
# --------------------------------------------
# Return a number between 3 and 9
# print(random.randint(3, 9))
# -------------------------------------
mylist = ["apple", "banana", "cherry","mango","pineapple","chiku"]
# mylist1 = ["apple", "banana", "cherry"]
# print(random.choice(mylist))
# print(random.choices(mylist1, k = 14))
# ------------------------------------------------------------
# random.shuffle(mylist)
# random.shuffle(mylist)
# print(mylist)
# ----------------------------------------
# Return a list that contains any 2 of the items from a list:
# print(random.sample(mylist, k=2))
# ---------------------------------------------
# Return a random number between, and included, 20 and 60:
# print(random.uniform(20, 60))
# ------------------------------------
# Return a random number between, and included, 20 and 60, but most likely closer to 20:
# print(random.triangular(20, 60, 30))
# print(random.randrange(10))
# print(random.randint())
# =====================================
# randomlist = []
# for i in range(0,5):
#     n=random.randint(1,30)
# randomlist.append(n)
# print(randomlist)
# ========================================
# import string
# import random
# N = 7
# res = ''.join(random.choices(string.ascii_uppercase +
#                              string.digits, k=N))
# print("The generated random string : " + str(res))
# --------------------------------------------
#EVEN NUMBERS
# print("Even Numbers")
# for x in range(20):
#     print(random.randrange(10, 100, 2),end=' '),
# print("\nOdd Numbers")
# for x in range(20):
#     print(random.randrange(5, 100, 2),end=' ')
# ------------------------------------------------------
# print("Select a random element from a list:")
# elements = [1, 2, 3, 4, 5]
# print(random.choice(elements))
# print(random.choice(elements))
# print("\nSelect a random element from a set:")
# elements = {1,2,3,4,5}
# # convert to tuple because sets are invalid inputs
# print(random.choice(tuple(elements)))
# print(random.choice(tuple(elements)))
# print(random.choice(tuple(elements)))
# print("\nSelect a random value from a dictionary:")
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# key = random.choice(list(d))
# print(d[key])
# key = random.choice(list(d))
# print(d[key])
# key = random.choice(list(d))
# print(d[key])
# print("\nSelect a random file from a directory.:")
# print(random.choice(os.listdir("/")))
# --------------------------------------------------
# import types
# def a(x):
#     yield x
#
# def b(x):
#     return x
#
# def add(x, y):
#     return x + y
#
# print(isinstance(a(456), types.GeneratorType))
# print(isinstance(b(823), types.GeneratorType))
# print(isinstance(add(8, 2), types.GeneratorType))
# ------------------------------------------------------------
# from decimal import Decimal
#
# def round_to_10_cents(x):
#     remainder = x.remainder_near(Decimal('0.10'))
#     if abs(remainder) == Decimal('0.05'):
#         return x
#     else:
#         return x - remainder
#
# for x in range(80, 120):
#     y = Decimal(x) / Decimal('1E2')
#     print("{0} rounds to {1}".format(y, round_to_10_cents(y)))