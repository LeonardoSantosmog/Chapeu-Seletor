# 🧙‍♂️ Sistema de Seleção de Casas de Hogwarts

Este é um pequeno projeto em Python que simula o famoso **Chapéu Seletor** de Hogwarts, do universo de Harry Potter. Ele faz três perguntas ao usuário e, com base nas respostas, determina pontos para as quatro casas: **Grifinória**, **Corvinal**, **Lufa-Lufa** e **Sonserina**.

## 🎯 Objetivo

Este projeto tem como objetivo praticar estruturas condicionais, entrada de dados e lógica de pontuação em Python, de forma divertida e interativa.

---

## 🚀 Como usar

1. Certifique-se de ter o **Python 3** instalado em seu computador.
2. Baixe ou clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

3. Execute o script no terminal:

```bash
python selecao_hogwarts.py
```

4. Responda às perguntas no terminal para descobrir para qual casa você seria enviado!

---

## 🧠 Perguntas e Pontuações

As perguntas são baseadas em preferências pessoais. Cada resposta contribui com pontos para determinadas casas.

Ao final, o programa mostra a pontuação total de cada casa.

---

## 🧾 Código-fonte

```python
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
```

---

## ✨ Resultado Esperado

O terminal exibirá a pontuação final de cada casa, com emojis representando as casas de Hogwarts. Você pode usar os resultados para ver com qual casa você mais se identifica!

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e de aprendizado. 🌟

---

## 🧙 Créditos

Criado por [LeonardoSantosmog](https://github.com/LeonardoSantosmog) ✨
