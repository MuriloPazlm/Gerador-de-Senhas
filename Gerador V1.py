from random import randint

senha = [(randint(0,10)),(randint(0,10)),(randint(0,10)),
         (randint(0,10)),(randint(0,10)),(randint(0,10)),
         (randint(0,10))]

print('-='*20)
print('Seja bem vindo ao seu gerador de senhas!')
print('-='*20)

v1 = str(input('Deseja gerar uma senha agora? (S/N)  ')).upper()
if v1 in "Ss":
    print('Que ótimo!')
    v2 = int(input('Quantos caracteres deseja? '))
    
    print(f'Aqui está sua senha gerada:')
    print("".join(map(str, senha)))
