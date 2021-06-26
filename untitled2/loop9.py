def contnum(n):
    num = 1

    for i in range(0, n):

        for j in range(0, i ):
            print(num, end=" ")

            num = num + 1

        print("\r")


n = input("Enter an integer")

contnum(n)