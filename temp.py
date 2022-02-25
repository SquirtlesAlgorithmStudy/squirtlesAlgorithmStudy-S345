def circularShift_right(a):
    result_list = ['0'] * 8
    for i in range(7):
        result_list[i+1] = a[i]
    result_list[0] = a[7]
    result = ''.join(result_list)
    return result


print(circularShift_right('00001111'))
