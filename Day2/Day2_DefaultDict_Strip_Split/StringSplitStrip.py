if __name__ == "__main__":

    a = "             "
    print(a.isspace())
    print(a.strip())
    print(len(a.strip()))

    b = "A: Anand"
    c = "A: Anand, P: priya"
    print(b.split(":"), len(b.split(":")))
    print(c.split(":"), len(c.split(":")))
