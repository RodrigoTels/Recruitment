def Verifica_CPF():
  cpf = input('digite seu cpf: ')
  CPF_enviado = cpf.replace('.','').replace('-','')
  nove_digitos = CPF_enviado[:9]


  contador_regressivo_1 = 10

  resultado_digito_1 = 0
  for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
  digito_1 = (resultado_digito_1 * 10) % 11
  digito_1 =digito_1 if digito_1 <= 9 else 0

  dez_digitos = nove_digitos + str(digito_1)
  contador_regressivo_2 = 11

  resultado_digito_2 = 0
  for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -=1
  digito_2 = (resultado_digito_2 * 10) % 11
  digito_2 = digito_2 if digito_2 <= 9 else 0

  CPF_Gerado = f'{nove_digitos}{digito_1}{digito_2}'

  if CPF_enviado == CPF_Gerado:
    print(f'O CPF: {CPF_enviado} é válido')
  else:
    print('CPF invalido')

Verifica_CPF()