def giaithua(n):
    #Tính giai thừa 1 số nhập từ bàn phím
    if n==1:
       return 1
    else:
       return (n*giaithua(n-1))
X=int(input("nhập số cần tính thứ 1!-->"))
X1=int(input("nhập số cần tính thứ 2!-->"))
X2=int(input("nhập số cần tính thứ 3!-->"))
print(" giai thưa của" ,X,"và",X1,"và" ,X2,"là",giaithua(X),"và",giaithua(X1),"và",giaithua(X2))