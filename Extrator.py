import requests

API_KEY = "d966860f1a7fa2fdab289bf508f96bc5"

print("Digite o nome da cidade para consulta")
cidade = input()
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] 
print(descricao, f"{temperatura}°C")
