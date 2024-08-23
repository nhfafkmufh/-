first = int(input())
second = int(input())
third = int(input())
if first == second or second == third or third == first:
    if first == second and second == third:
        print(3)
    else:
        print(2)
else:
    print(0)