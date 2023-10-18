peso : float = float(input("Qual seu peso?"))
altura : float = float(input('Qual sua altura?'))

calculoimc = peso / (altura * altura)
print('O seu IMC é de :', calculoimc)

if calculoimc < 18.5:
    print('Sua classificação é: Magreza')

elif calculoimc >= 18.5 and calculoimc <= 24.9:
    print('Sua classificação é: Normal')

elif calculoimc >= 25 and calculoimc <= 29.9:
    print('Sua classificação é: Sobrepeso')

elif calculoimc >= 30 and calculoimc <= 34.9:
    print('Sua classificação é: Obesidade grau I')

elif calculoimc >= 35 and calculoimc <= 39.9:
    print("Sua classificação é: Obesidade grau II")

elif calculoimc >= 40:
    print('Sua classificação é: Obesidade grau III')
    
else:
    print('Refaça sua operação!!')