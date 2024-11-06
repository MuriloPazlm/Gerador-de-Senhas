from random import randint

senha = [(randint(0,10)),(randint(0,10)),(randint(0,10)),
         (randint(0,10)),(randint(0,10)),(randint(0,10)),
         (randint(0,10)),(randint(0,10)),(randint(0,10)),
         (randint(0,10))]
v1= 0

print('-='*20)
print('Seja bem vindo ao seu gerador de senhas!')
print('-='*20)

v1 = str(input('Deseja gerar uma senha agora? (S/N)  ')).upper()
while v1 not in "SsNn":
    print('Por favor digite apenas S ou N!')
    v1 = str(input('Deseja gerar uma senha agora? (S/N)  ')).upper()

if v1 in "Ss":
    print('Que ótimo!')
    v2 = int(input('Quantos caracteres de 1 a 10 deseja? '))
    print('Aqui está sua senha gerada:')
    print(f"".join(map(str, senha[0:v2])))
