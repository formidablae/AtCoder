N_length = int(input())
T_string = input()

if len(T_string) == 1:
    if T_string == '1':
        print(2 * 10**10)
    else:
        print(10**10)
elif len(T_string) == 2:
    if T_string == '11':
        print(10**10)
    elif T_string == '10':
        print(10**10)
    elif T_string == '01':
        print(10**10 - 1)
    else:
        print(0)
elif len(T_string) == 3:
    if T_string == '110':
        print(10**10)
    elif T_string == '101':
        print(10**10 - 1)
    elif T_string == '011':
        print(10**10 - 1)
    else:
        print(0)
else:
    flag_zero = False
    for i in range(0, N_length - 2):
        sample = T_string[i: i + 3]
        if sample != '110' and sample != '101' and sample != '011':
            flag_zero = True
            break
    if flag_zero:
        print(0)
    else:
        zero_counter = T_string.count('0')
        if T_string[0:2] == '01' and T_string[-1] == '0':
            print(10**10 - zero_counter + 1)
        elif T_string[0:2] == '11' and T_string[-1] == '0':
            print(10**10 - zero_counter + 1)
        else:
            print(10**10 - zero_counter)
