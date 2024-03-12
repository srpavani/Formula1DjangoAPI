from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import F1ResultModels
from .serializers import F1ResultSerializer
from bs4 import BeautifulSoup
import json
#from .busca import buscarGrid
import requests


class F1ResultView(ModelViewSet):
    queryset = F1ResultModels.objects.all()
    serializer_class = F1ResultSerializer
    
    def create(self, request):  
        try:  
            request = requests.get("https://www.formula1.com/en/results.html/2023/races.html")
            scrap = BeautifulSoup(request.text, "html.parser")

            dados = scrap.find_all("tr")

            ListaCorridas = []

            for dado in dados[1:]:  
                columns = dado.find_all("td")
                if len(columns) == 0: 
                    continue
                listaDados = {
                    "GrandPix": columns[1].text.strip(),
                    "data": columns[2].text.strip(),
                    "vencedor": columns[3].text.strip(),
                    "time": columns[4].text.strip(),
                    "voltas": columns[5].text.strip(),
                }
                ListaCorridas.append(listaDados)

            for listaDados in ListaCorridas:
                grandpx = listaDados.get('GrandPix', '')
                dt = listaDados.get('data', '')  # Corrigido para 'Data' em vez de 'data'
                vencedor = listaDados.get('vencedor')
                time = listaDados.get('time')
                voltas = listaDados.get('voltas')
                
                dados_recebido = {
                    "GrandPix": grandpx,
                    "data": dt,
                    "vencedor": vencedor,
                    "time": time,
                    "voltas": voltas
                }
                
                serializer = F1ResultSerializer(data=dados_recebido)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e: 
            print("error:", str(e))
            return Response({"error": "Erro interno do servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
