class Solution:
    # @param A : list of integers
    # @return a list of integers


    def plusOne(self, A):
        pass


A = input("input: ")

# B = [int(c) for c in str(int("".join([str(n) for n in A])) + 1)]
# print(B)

a = [str(i) for i in A]
b = "".join(a)
c = int(b) + 1
d = [int(d) for d in str(c)]

print(d)


#
# z = [str(n) for n in A]
# print(z)
# print(type(z))
#
# a = "".join(z)
# print(a)
# print(type(a))
#
# s = str(a)
# print("s: ", s)
# print(type(s))
#
# b = (int(a) + 1)
# print(b)
# print(type(b))
#
# x = [int(c) for c in str(b)]
# print(x)
# print(type(x))
