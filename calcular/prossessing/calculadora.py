

def somar(a,b):
    return a+b

def subitrair(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a//b

def calculadora():
    print("qual conta gostaria de fazer")
    a=-1
    while(a!=0):
        print(f'digite \n1-Para soma\n2-Para subtração\n3-Para multiplicação\n4-Para divisão')
        a= int(input())
        if(a==1):
            print ("digite os dois valores")
            valor1,valor2= input().split()
            print(somar(int(valor1),int(valor2)))
        elif(a==2):
            print ("digite os dois valores")
            valor1,valor2= input().split()
            print(subitrair(int(valor1),int(valor2)))
        elif(a==3):
            print ("digite os dois valores")
            valor1,valor2= input().split()
            print(mult(int(valor1),int(valor2)))
        elif(a==4):
            print ("digite os dois valores")
            valor1,valor2= input().split()
            print(div(int(valor1),int(valor2)))
calculadora()