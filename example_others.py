def pair_for_value(items, total):
    for i in range(len(items)):
        for j in range(len(items)-1):
            if items[i] + items[j] == total:
                print(items[i], items[j])


pair_for_value([2, 3, 4, 5, 6, 7, 1], 10)


def string_reverse(str):
    new = ""
    for s in str:
        new = s + new
    print(new)


string_reverse('shubhneet')


def recursion_reverse(s):
    if len(s) <= 1:
        return s
    else:
        return recursion_reverse(s[1:]) + s[0]


print(recursion_reverse("shubhneet"))
