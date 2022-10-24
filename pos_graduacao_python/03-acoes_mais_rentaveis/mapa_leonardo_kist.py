"""
UNICESUMAR - Pós-Graduação em Desenvolvimento de Sistemas com Python
MATÉRIA DA DISCIPLINA: Python Avançado
ALUNO: LEONARO HENRIQUE MARIN KIST
"""


#IMPORTAÇÃO
from kivy.lang import  Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import  FloatLayout
from kivy.uix.label import Label
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from kivy.core.window import Window
Window.size = (1000, 800)


#classe do widget Corpo
class Corpo(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #função para realizar as ações ao clicar no botão
    def obter(self):

        #lista dos ativos que serão obtidos os dados
        lista_ativos = ['ABEV3.SA','ALPA4.SA','AMER3.SA','ASAI3.SA','AZUL4.SA','B3SA3.SA','BBAS3.SA','BBDC3.SA','BBDC4.SA','BBSE3.SA','BEEF3.SA','BIDI11.SA','BPAC11.SA','BPAN4.SA','BRAP4.SA','BRFS3.SA','BRKM5.SA','BRML3.SA','CASH3.SA','CCRO3.SA','CIEL3.SA','CMIG4.SA','CMIN3.SA','COGN3.SA','CPFE3.SA','CPLE6.SA','CRFB3.SA','CSAN3.SA','CSNA3.SA','CVCB3.SA','CYRE3.SA','DXCO3.SA','ECOR3.SA','EGIE3.SA','ELET3.SA','ELET6.SA','EMBR3.SA','ENBR3.SA','ENEV3.SA','ENGI11.SA','EQTL3.SA','EZTC3.SA','FLRY3.SA','GGBR4.SA','GOAU4.SA','GOLL4.SA','HAPV3.SA','HYPE3.SA','IGTI11.SA','IRBR3.SA','ITSA4.SA','ITUB4.SA','JBSS3.SA','JHSF3.SA','KLBN11.SA','LCAM3.SA','LREN3.SA','LWSA3.SA','MGLU3.SA','MRFG3.SA','MRVE3.SA','MULT3.SA','NTCO3.SA','PCAR3.SA','PETR3.SA','PETR4.SA','PETZ3.SA','POSI3.SA','PRIO3.SA','QUAL3.SA','RADL3.SA','RAIL3.SA','RDOR3.SA','RENT3.SA','RRRP3.SA','SANB11.SA','SBSP3.SA','SLCE3.SA','SOMA3.SA','SULA11.SA','SUZB3.SA','TAEE11.SA','TIMS3.SA','TOTS3.SA','UGPA3.SA','USIM5.SA','VALE3.SA','VBBR3.SA','VIIA3.SA','VIVT3.SA','WEGE3.SA','YDUQ3.SA']

        #obter os ativos com a biblioteca yfinance nos ultimos 6 meses
        ativos = yf.download(tickers=lista_ativos, period='6mo')
        ativos_close = ativos['Adj Close']
        
        #manipulação dos dados para transformar em percentual
        percent_alt = ativos_close.pct_change()
        percent_acumulado = (1 + percent_alt).cumprod()
        percent_acumulado.iloc[0]=1

        #calcula a diferença do valor do ativo entre o último dia menos o primeiro dia
        #isso se faz necessário para poder obter os ativos que obtiveram a maior rentabilidade no final do prazo de seis meses 
        percent_dif = (percent_acumulado.iloc[-1])-(percent_acumulado.iloc[0])
        
        #obtem os 10 ativos com maior rentabilidade
        top_dez_percent = percent_dif.nlargest(n=10)*100
        #cria uma lista com o nome dos ativos
        top_dez_list = list(top_dez_percent.index.values)

        #retorna os dados de fechamento em percentual dos 10 melhores ativos
        top_dez = percent_acumulado.loc[:,top_dez_list]
        
        #definição do gráfico
        courses = list(top_dez_percent.index)
        values = list(top_dez_percent.values)
        plt.bar(courses, values, color ='blue', width = 0.4)
        plt.xlabel("Ativos")
        plt.ylabel("Rentabilidade [%]")
        plt.title("Rentabilidade dos Ativos")

        #impressão do gráfico na tela
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette =  "BlueGray"
        Builder.load_file('mapa_leonardo_kist.kv')
        return Corpo()


MainApp().run()