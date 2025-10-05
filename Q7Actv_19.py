def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
n=int(input("Veuillez entrer un nombre entier positif n="))
while n<0:
    print("Le nombre doit être positif ou nul")
    n=int(input("Veuillez entrer un nombre entier positif n="))

for i in range(n+1):
    print(f"U{i}={Fibonacci(i)}")