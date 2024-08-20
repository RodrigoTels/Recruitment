import time
def MensagemMãe():
  palavra_secreta = 'Mamãe'
  letra_correta = ''
  palavra_tentada = ''
  tentativa = 0
  print('------- Descubra a palavra secreta -------', end='\n')
  print('-- Conside letras maiusculas e minusculas --')


  while len(palavra_tentada) < len(palavra_secreta):
    letra_digitada = input('digite uma letra:  ')
    tentativa += 1

    if letra_digitada == 'sair':
      break

    if letra_digitada in palavra_secreta:
        letra_correta = letra_digitada
        palavra_tentada += letra_correta
    else:
      print('--------- letra incorreta ---------')

    for letra in palavra_secreta:
      if letra in palavra_tentada:
        print(letra, end='', sep=' ')
      else:
        print('*', end='')

    if letra_digitada == palavra_secreta:
      print(f'--------- Acertou Parabéns ---------')
      print(f'A palavra era {palavra_secreta}')
      print(f'Você acertou em: {tentativa} tentativas')
      print('Mamãe, se esta vendo essa mensagem é porque descobriu para quem é a mensagem secreta', end='\n')
      print('Feliz dia das mães, só tenho a agradecer, fiz esse breve joguinho para mostrar a enor- ', end='\n')
      print('me diferença que seu apoio e compreensão fizeram na minha vida, e no meu conhecimento ', end='\n')
      print('Obrigado por tudo! Te amo muito')
      break

#ativar = input('--- Quer descobrir para quem é a mensagem secreta? [S]im? [N]ão? ---').upper()

while True:

  ativar = input('--- Quer descobrir para quem é a mensagem secreta? [S]im? [N]ão? ---').upper()

  if len(ativar) > 1:
    print('Digite apenas S para Sim ou N para Não')
    continue

  if ativar == 'N':
    print('--- Até mais, e obrigado! ---')
    time.sleep(2)
    break

  if ativar == 'S':
   MensagemMãe()

