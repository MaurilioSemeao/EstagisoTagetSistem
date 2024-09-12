## Exercico 01
# A variavel "ele" se refere a quantidade de elementos que vai ter na lisna 
# nesse caso sao 5 elementos 
# A variavel "bas" representa a base por onde comessa a sequencia 
def exercicio01():
    ele = 5
    bas = 1
    strin = ''
    for i in range(ele):
        strin += f"{bas},"
        bas +=2

    return strin

## Exercicio 02
def exercicio02():
    ele = 7
    bas = 2
    strin = ''
    for i in range(ele):
        strin += f"{bas},"
        bas *=2

    return strin

## Exercico 03
def exercicio03():
    ele = 5
    bas = 0
    strin = ''
    for i in range(ele):
        strin += f"{bas},"
        bas = i ** 2

    return strin

## Exercico 04
def exercicio04():
    ele = 5
    bas = 2
    strin = ''
    for i in range(ele):
        strin += f"{bas ** 2},"
        bas += 2 

    return strin

## Exercicio 05
def exercicio05():
    ele = 8
    count = 0
    a,b = 0,1
    string = f"{a},"
    while count < ele :
        a,b = b,a+b
        string += f"{a},"
        count += 1

    return string

print(exercicio04())