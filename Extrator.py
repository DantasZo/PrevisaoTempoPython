from sys import orig_argv
import requests
import chave

API_KEY = chave.chave(chamado=orig_argv)
print(API_KEY)

print("Digite o nome da cidade para consulta")
cidade = input()
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp']
print(descricao, f"{temperatura}°C")
