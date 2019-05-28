def ruler():
    x = int(input("Input the value of ruler:  "))
    i = 1
    a1 = ""
    a2 = " "
    while (i <= x):
        a1 += str(i % 10)
        i += 1
        if (i % 10 == 0):
            a2 += str(int(i / 10))
        else:
            a2 += " "
    print("\n")
    print(x)
    print(a2)
    print(a1)


ruler()