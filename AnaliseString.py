import time

nome = input('Digite o seu nome completo: ').strip()
nome_sem_espaco = len(nome) - nome.count(' ')
primeiro_nome = nome.split()
time.sleep(1.2)
print('Processando dados...')
time.sleep(2.5)

print(f'Seu nome com letras maiúsculas: {nome.upper()}')
print(f'Seu nome com letras minúsculas: {nome.lower()}')
print(f'Seu nome tem {nome_sem_espaco} letras')
print(f'Seu primeiro nome tem: {len(primeiro_nome[0])} caracteres')