from collections import Counter

def deletionCounter(a,b):
    dict_a = Counter(a)

    counter = 0

    for i in b:
        if i in dict_a:
            if dict_a[i] <= 0:
                counter += 1
            else:
                dict_a[i] -= 1
        else:
            counter+=1
    return sum(dict_a.values()) + counter

def main():

    a = str(input("Enter string 1: "))
    b = str(input("Enter string 2: "))

    print("It takes %d deletions to make an anagram" % deletionCounter(a,b))


if __name__ == "__main__":
    main()