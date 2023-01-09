import requests
from tkinter import *
from datetime import date
from pokedex import pokemon_lista

#Buscar valor do dólar
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
dolar = cotacao_dolar[:4]

## Pra pegar o pokémon
inteiro = (int(dolar.replace(".", "")))

#print("Cotação atual do dólar")
valor_atual = (f"R$: {dolar}")

##Foto e nome do pokémon
normal = f"imagens/normal/{inteiro}.png"
shiny = f"imagens/shiny/{inteiro}.png"
missingno = "imagens/missingno.png"

#Dia da semana
dias = [
    "segunda",
    "terça",
    "quarta",
    "quinta",
    "sexta",
    "sábado",
    "domingo"
]

data = date.today()
indice = data.weekday()
dia_da_semana = dias[indice]

if dia_da_semana == "sábado" or dia_da_semana == "domingo":
    dia_da_semana = shiny
else:
    dia_da_semana = normal

if inteiro > 649:
    dia_da_semana = missingno
else:
    dia_da_semana = dia_da_semana

#Nome do Pokémon
nome_do_pokemon = pokemon_lista[inteiro-1]

#Configurações da janela
programa = Tk()
programa.title("PokéDólar")
programa.geometry("400x360")
programa.eval('tk::PlaceWindow . center')
programa.resizable(0,0)
programa.iconbitmap("imagens/icon.ico")

#Imagem de fundo
bg= PhotoImage(file="imagens/bg.png")
my_label = Label(programa,image=bg)

# Criar menu
minha_janela = Canvas(programa)
minha_janela.pack(fill="both", expand=True)

# Seleciona imagem canvas
minha_janela.create_image(0,0, image=bg, anchor="nw")

#Valor do dólar
minha_janela.create_text(200, 132, text=f"{valor_atual}", font=("Rockwell Extra Bold",16), anchor="center")

# Imagem do Pokémon
imagem_do_pokemon = PhotoImage(file=f"{dia_da_semana}")
minha_janela.create_image(201,223, image=imagem_do_pokemon)

##Nome do Pokémon
minha_janela.create_text(200,307, text=f"{nome_do_pokemon}", font=("Rockwell Extra Bold",12), anchor="center",fill="white")

programa.mainloop()
