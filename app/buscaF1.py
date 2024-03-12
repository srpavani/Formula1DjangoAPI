from bs4 import BeautifulSoup
import requests
import json

page_to_scrape = requests.get("https://www.formula1.com/en/results.html/2024/races.html")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

pilotos = soup.find_all("tr")

drivers_list = []

for piloto in pilotos[1:]:  
    coluna = piloto.find_all("td")
    if len(coluna) == 0: 
        continue
    driver_data = {
        "posssition": coluna[0].text.strip(),
        "Posicao": coluna[1].text.strip(),
        "Piloto": coluna[2].text.strip(),
        "nacionalidade": coluna[3].text.strip(),
        "equipe": coluna[4].text.strip(),
    }
    drivers_list.append(driver_data)




# Para acessar o atributo 'equipe' de cada dicionário dentro da lista drivers_list
for driver_data in drivers_list:
    #print(driver_data)
    grandpx = driver_data.get('Posicao')
    dt = driver_data.get('Piloto')
    time = vencedor= driver_data.get('nacionalidade')
    voltas =  driver_data.get('equipe')




    dados_recebido = {
                    "Posssicao": grandpx,
                    "Piloto": dt,
                    "nacionalidade": vencedor,
                    "time": time,
                    "equipe": voltas
                }
    
    
  