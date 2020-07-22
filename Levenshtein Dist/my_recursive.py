def dist(a, b):
    if a == "":
        return len(b)
    if b == "":
        return len(a)
    if a[0] == b[0]:
        return dist(a[1:], b[1:])
    return 1 + min(dist(a, b[1:]), dist(a[1:], b), dist(a[1:], b[1:]))

if __name__ == "__main__":
    a = input("String A: ")
    b = input("String B: ")
    print(dist(a, b))