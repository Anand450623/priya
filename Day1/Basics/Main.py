from Day1.Basics.Utils import generator, gcd


if __name__ == "__main__":

    a = generator()
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())

    print(f"The required gcd is = {gcd(5, 30)}")

    for i in range(10):
        print(i, end=" ")
        i += 2

    print()
    text = "priya"
    print(f"{text} is bad girl.")
