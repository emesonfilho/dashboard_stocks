from dashboard import dados_dowload

from tkinter import *
import investpy as inv
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk, FigureCanvasTkAgg
import matplotlib.backends as tkagg

from matplotlib.figure import Figure

import numpy as np


class Janela_Dashboard:
    def __init__(self, master = None):
        self.master = master
        self.bg_color = 'white'

        self.pegando_dados_acoes = list()
        self.pegando_dados_indices = list()

        self.container1()
        self.containers2()

    def container1(self):

        self.primeiro_container = Frame(self.master)
        self.primeiro_container['pady'] = 10
        self.primeiro_container['bg'] = self.bg_color
        self.primeiro_container.grid(row = 0, column = 0)


        Label(self.primeiro_container, text="Código do papel").grid(row = 0, column = 0)


        Label(self.primeiro_container, text="Salvar").grid(row=3, column=0)

        Label(self.primeiro_container, text="País do papel").grid(row = 4, column = 0)

        Label(self.primeiro_container, text="Data início").grid(row=5, column=0)

        Label(self.primeiro_container, text="Data final").grid(row=6, column=0)

        Label(self.primeiro_container, text="Preço de ref").grid(row=7, column=0)

        Label(self.primeiro_container, text="Plot").grid(row=8, column=0)

        Label(self.primeiro_container, text="Clear").grid(row=9, column=0)


    def containers2(self):

        self.segundo_container = Frame(self.master)
        self.segundo_container['pady'] = 10
        self.segundo_container['bg'] = self.bg_color
        self.segundo_container.grid(row= 0, column=1)

        self.acoes_entrada = Entry(self.segundo_container)
        self.acoes_entrada.grid(row = 0, column = 0)

        Button(self.segundo_container, text="Pegar", command=self.pegando_papeis).grid(row=1, column=0)

        self.pais_entrada = Entry(self.segundo_container)
        self.pais_entrada.grid(row=4, column=0)

        self.data_inicio_entrada = Entry(self.segundo_container)
        self.data_inicio_entrada.grid(row=5, column=0)

        self.data_final_entrada = Entry(self.segundo_container)
        self.data_final_entrada.grid(row=6, column=0)

        self.preco_ref = Entry(self.segundo_container)
        self.preco_ref.grid(row=7, column=0)

        Button(self.segundo_container, text = "Gerar",command = self.construindo_grafico).grid(row = 8, column = 0)

        Button(self.segundo_container, text="Clear", command=self.deletando_dados).grid(row=9, column=0)


    def pegando_papeis(self):

        papel = self.acoes_entrada.get()

        self.pegando_dados_acoes.append(papel)

        print(self.pegando_dados_acoes)

    def deletando_dados(self):

        self.pegando_dados_acoes.clear()

    def construindo_grafico(self):

        dados = dados_dowload.Historical_data(
            self.data_inicio_entrada.get(), self.data_final_entrada.get(),self.pais_entrada.get()
        ).historico_acoes(self.pegando_dados_acoes, status = self.preco_ref.get())

        self.terceiro_container = Frame(self.master)
        self.terceiro_container.grid(row=0, column=2)

        # Construindo o objeto figura

        grafico= Figure(figsize=(10, 6), dpi=100, edgecolor='red', facecolor='white')

        # Adicionando um gráfico a ele
        grafico_tela= grafico.add_subplot(111)


        # Adicionando um título a ele
        grafico_tela.set_title('Comprando ações')


        if len(self.pegando_dados_acoes) != 1:
            dados = (dados / dados.iloc[0])

        else:
            dados = dados[self.preco_ref.get()]


        # Adicionando os dados no gráfico
        grafico_tela.plot(dados.index, dados)

        # Adicionando a legenda
        grafico_tela.legend(self.pegando_dados_acoes, loc=0)

        canvas = FigureCanvasTkAgg(grafico, self.terceiro_container)
        canvas.draw()

        # Adcionando a barra de configurações do gráfico
        barra_de_ferramentas = NavigationToolbar2Tk(canvas, self.terceiro_container)

        barra_de_ferramentas.update()

        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)






root = Tk()
Janela_Dashboard(root)
root.mainloop()




