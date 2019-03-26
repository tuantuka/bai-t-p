for x in range(0,100):
    for i in range(2,x):
        if x%i==0:
            j=x/i
            print(x,"không phải là số nguyên tố")
            break
        else:
            print(x,"là số nguyên tố ")
