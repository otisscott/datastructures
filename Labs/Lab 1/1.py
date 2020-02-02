def add_binary(bin_num1, bin_num2):
    maxi = 1
    if len(bin_num1) >= len(bin_num2):
        maxi = len(bin_num1)
    else:
        maxi = len(bin_num2)

    bin_num1 = bin_num1.zfill(maxi)
    bin_num2 = bin_num2.zfill(maxi)

    final = ''
    carry = 0
    for i in range(maxi - 1, -1, -1):
        num1 = int(bin_num1[i])
        num2 = int(bin_num2[i])
        extra = carry
        if num1 == 1:
            extra += 1
        if num2 == 1:
            extra += 1
        if extra % 2 == 1:
            final += '1'
        else:
            final += '0'
        if extra < 2:
            carry = 0
        else:
            carry = 1
    if carry > 0:
        final = '1' + final
    return final


print(add_binary("11", "1"))
