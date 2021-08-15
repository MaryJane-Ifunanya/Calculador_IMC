altura = float(input('Qual é a us aaltura em cm:'))
peso = float(input('Qual é o seu peso em kg:'))

IMC = peso / (altura/100)**2

if IMC < 18.5:
    print(f'Seu IMC é de \033[32m{IMC:.2f}\033[m, e é classificado como \033[35mMagresa\033[m.')
elif IMC >= 18.5 and IMC < 24.9:
    print(f'Seu IMC é de \033[32m{IMC:.2f}\033[m, e é classificado como \033[34mNormal\033[m.')
elif IMC >= 25 and IMC < 29.9:
    print(f'Seu IMC é de \033[32m{IMC:.2f}\033[m, e é classificado como \033[36mSobrepeso, mas bem pouco\033[m.')
elif IMC >= 30 and IMC < 39.9:
    print(f'Seu IMC é de \033[32m{IMC:.2f}\033[m, e é classificado como \033[31mObesidade\033[m.')
else:
    print('\033[31mPode parar de comer e começar a malhar pois o negocio está feio! Obesidade Grave!!!\033[m')
