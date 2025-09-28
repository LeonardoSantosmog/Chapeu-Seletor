# Sistema de Seleção de Casas de Hogwarts
# Pontuações das casas
grifinoria = 0
corvinal = 0
lufa_lufa = 0
sonserina = 0

# Q1
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

resposta = int(input("Escolha (1 ou 2): "))

if resposta == 1:
    grifinoria += 1
    corvinal += 1
elif resposta == 2:
    lufa_lufa += 1
    sonserina += 1
else:
    print("Entrada errada")

# Q2
print("\nQ2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

resposta = int(input("Escolha (1, 2, 3 ou 4): "))

if resposta == 1:
    lufa_lufa += 2
elif resposta == 2:
    sonserina += 2
elif resposta == 3:
    corvinal += 2
elif resposta == 4:
    grifinoria += 2
else:
    print("Entrada errada")

# Q3
print("\nQ3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

resposta = int(input("Escolha (1, 2, 3 ou 4): "))

if resposta == 1:
    sonserina += 4
elif resposta == 2:
    lufa_lufa += 4
elif resposta == 3:
    corvinal += 4
elif resposta == 4:
    grifinoria += 4
else:
    print("Entrada errada")

# Resultado final
print("\nPontuação final:")
print("🦁 Grifinória:", grifinoria)
print("🦅 Corvinal:", corvinal)
print("🦡 Lufa-Lufa:", lufa_lufa)
print("🐍 Sonserina:", sonserina)
