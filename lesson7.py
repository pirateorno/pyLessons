#
#
# def division(a, b):
#     res = 0
#     try:
#         res = a/b
#
#     except:
#         try:
#             a = int(a)
#             b = int(b)
#             res = a / b
#         except ZeroDivisionError:
#             res = 0
#         except ValueError:
#             res = "Enter number"
#     print(res)
#
# while division.res == 0:
#     division(input(), input())
# x = 10
# try:
#     print(x)
# except:
#     print("Something went wrong")
# else:
#     print("Else program do")
# finally:
#     print("Th program has completd it`s work")

# def checker(var1):
#     if type(var1) != str:
#         raise TypeError(f"Sorry, we cant work with {type(var1)} we need clas str")
#     else:
#         return var1
# fir = 10
# checker(fir)

# class BuildingError(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot be built!"
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         print("Enough material")
#     else:
#         raise BuildingError(amount_of_material)
#
# materials = 1
# check_material(materials, 300)

import warnings
warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("Warning, no code here", SyntaxWarning)
warnings.warn("Warning, module not import", ImportWarning)


