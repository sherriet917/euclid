"""
Uses the Euclidean Algorithm to compute the GCD of two numbers.

Performs each row operation on an identity matrix to perform the
Extended Euclidean Algorithm and compute Bezout coefficients.
"""

# assumes n1 > n2


def row_op(n1, n2):
    c = 0
    while n1 - n2 >= 0:
        c += 1  # determine scalar
        n1 -= n2
        if n1 == 0 or n2 == 0:
            return (c, n1, n2)
    return (c, n1, n2)


n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))

# retain copy of original integers to build Bezout's identity later
o1 = n1
o2 = n2

if n1 == n2:
    print("Both integers are the same. GCD is trivial. ")

r1 = [1, 0]
r2 = [0, 1]

step = 1

# algorithm terminates when either integer is 0
while n1 != 0 and n2 != 0:

    c = 1
    if n1 >= n2:
        c, n1, n2 = row_op(n1, n2)
        # need to do r1 = r1 - cr2
        r1[0] = r1[0] - c * r2[0]
        r1[1] = r1[1] - c * r2[1]

    elif n2 > n1:
        c, n2, n1 = row_op(n2, n1)
        # need to do r2 = r2 - cr1
        r2[0] = r2[0] - c * r1[0]
        r2[1] = r2[1] - c * r1[1]

    print("\n" + "The current step number is: " + str(step))
    print("c is equal to: " + str(c))
    print("Current matrix is: ")
    print(r1)
    print(r2)

    step += 1

print("\n" + "Algorithm has terminated.")
print("n1 is: " + str(n1))
print("n2 is: " + str(n2))

if n1 != 0:  # n1 is the GCD
    print("\n" + "The GCD is: " + str(n1))
    print("The Bezout coefficients are: " + str(r1[0]) + ", " + str(r1[1]))
    print("Bezout's identity: " +
          str(r1[0]) + "*" + str(o1) + " + " + str(r1[1]) + "*" + str(o2) + " = " + str(n1))
else:  # n2 is the GCD
    print("\n" + "The GCD is: " + str(n2))
    print("The Bezout coefficients are: " + str(r2[0]) + ", " + str(r2[1]))
    print("Bezout's identity: " +
          str(r2[0]) + "*" + str(o1) + " + " + str(r2[1]) + "*" + str(o2) + " = " + str(n2))
