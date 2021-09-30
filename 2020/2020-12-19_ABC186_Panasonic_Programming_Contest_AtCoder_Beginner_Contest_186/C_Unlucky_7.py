N = int(input())
int_N = N
wrongs = 0
while int_N >= 7:
    if "7" in str(int_N) or "7" in str(oct(int_N)):
        wrongs += 1
    int_N -= 1
print(N - wrongs)