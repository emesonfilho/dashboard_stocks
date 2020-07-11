from dashboard import dados_dowload

from tkinter import *
import investpy as inv
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk, FigureCanvasTkAgg
import matplotlib.backends as tkagg
from tkinter import ttk

import seaborn as sn

from matplotlib.figure import Figure

import numpy as np

from controle_menu import ajustando_menu
from dashboard import dados_dowload

class Janela_Dashboard:
    def __init__(self, master = None):
        root = Tk()
        root['bg'] = 'gray'
        root.title("Dashboard")

        self.master = master

        self.bg_color = 'gray'
        self.background_color = 'orange'

        self.pegando_dados_acoes = list()
        self.pegando_dados_indices = list()

        self.container1()
        self.container2()
        self.container4()

        ajustando_menu.Menu_user(referencia=root)
        root.mainloop()

    def container1(self):

        self.primeiro_container = Frame(self.master)
        self.primeiro_container['pady'] = 10
        self.primeiro_container['bg'] = self.bg_color
        self.primeiro_container.grid(row = 0, column = 0)


        Label(self.primeiro_container, text="Paper code", background = self.background_color).grid(row = 0, column = 0)


        Label(self.primeiro_container, text="Save", background = self.background_color).grid(row=3, column=0)

        Label(self.primeiro_container, text="Country of paper", background = self.background_color).grid(row = 4, column = 0)

        Label(self.primeiro_container, text="Start date", background = self.background_color).grid(row=5, column=0)

        Label(self.primeiro_container, text="Final date", background = self.background_color).grid(row=6, column=0)

        Label(self.primeiro_container, text="Reference price", background = self.background_color).grid(row=7, column=0)

        Label(self.primeiro_container, text="Plot", background = self.background_color).grid(row=8, column=0)

        Label(self.primeiro_container, text="Clear", background = self.background_color).grid(row=9, column=0)


    def container2(self):

        self.segundo_container = Frame(self.master)
        self.segundo_container['pady'] = 10
        self.segundo_container['bg'] = self.bg_color
        self.segundo_container.grid(row= 0, column=1)

        self.acoes_entrada = Entry(self.segundo_container)
        self.acoes_entrada.grid(row = 0, column = 0)

        Button(self.segundo_container, text="Take", command=self.pegando_papeis,
               background = self.background_color).grid(row=1, column=0)

        self.pais_entrada = Entry(self.segundo_container)
        self.pais_entrada.grid(row=4, column=0)

        self.data_inicio_entrada = Entry(self.segundo_container)
        self.data_inicio_entrada.grid(row=5, column=0)

        self.data_final_entrada = Entry(self.segundo_container)
        self.data_final_entrada.grid(row=6, column=0)

        self.preco_ref = Entry(self.segundo_container)
        self.preco_ref.grid(row=7, column=0)


        Button(self.segundo_container, text = "Generate",command = self.construindo_grafico,
               background = self.background_color).grid(row = 8, column = 0)

        Button(self.segundo_container, text="Clear", command=self.deletando_dados,
               background = self.background_color).grid(row=9, column=0)


    def pegando_papeis(self):

        papel = str(self.acoes_entrada.get()).upper()

        self.pegando_dados_acoes.append(papel)

    def deletando_dados(self):

        self.pegando_dados_acoes.clear()

    def construindo_grafico(self):



        dados = dados_dowload.Historical_data(
            self.data_inicio_entrada.get(), self.data_final_entrada.get(),str(self.pais_entrada.get()).upper()
        ).historico_acoes(self.pegando_dados_acoes, status = self.preco_ref.get())


        self.terceiro_container = Frame(self.master)
        self.terceiro_container.grid(row=0, column=2)

        # Construindo o objeto figura
        sn.set()
        grafico= Figure(figsize=(10, 6), dpi=100, edgecolor='red', facecolor='white')

        # Adicionando um gráfico a ele
        grafico_tela= grafico.add_subplot(111)


        # Adicionando um título a ele
        grafico_tela.set_title('Comparing actions')


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



    def enviando_dados(self):
        return self.pegando_dados_acoes


    def container4(self):
        # Esse container vai ser responsável por chamar a tela de informar os dados contábeis das empresas
        self.quarto_container = Frame(self.master)
        self.quarto_container['pady'] = 10
        self.quarto_container['bg'] = self.bg_color
        self.quarto_container.grid(row=1, column=0, columnspan = 2)

        Button(self.quarto_container, text="Contact Information", command=self.TelaContabil,
               background=self.background_color).grid(row = 0, column=0)



    def TelaContabil(self):
        # Criando a tela em que os dados vão ser chamados
        self.contabil = Toplevel()
        self.bg_color = 'gray'
        self.background_color = 'orange'

        self.contabil['bg'] = self.bg_color
        self.contabil.title('accounting')

        self.ver_contabil()

    def ver_contabil(self):
        # Aqui é onde arrumamos a grade onde os dados são plotados
        self.contabil.resizable(False, False)
        self.tree_eventos = ttk.Treeview(self.contabil, selectmode="browse",
                                         column=("column1", "column2", "column3","column4","column5",
                                                 "column6", "column7", "column8", "column9", "column10"),
                                         show='headings')
        self.tree_eventos.column("column1", width=60, minwidth=500, stretch=NO)
        self.tree_eventos.heading('#1', text='TICKER')

        self.tree_eventos.column("column2", width=60, minwidth=500, stretch=NO)
        self.tree_eventos.heading('#2', text='PRECO')

        self.tree_eventos.column("column3", width=60, minwidth=500, stretch=NO)
        self.tree_eventos.heading('#3', text='P/L')

        self.tree_eventos.column("column4", width=60, minwidth=500, stretch=NO)
        self.tree_eventos.heading('#4', text='DY')

        self.tree_eventos.column("column5", width=60, minwidth=500, stretch=NO)
        self.tree_eventos.heading('#5', text='P/VP')

        self.tree_eventos.column("column6", width=60, minwidth=500, stretch=NO)
        self.tree_eventos.heading('#6', text='EV/EBIT')

        self.tree_eventos.column("column7", width=60, minwidth=500, stretch=NO)
        self.tree_eventos.heading('#7', text='ROE')

        self.tree_eventos.column("column8", width=60, minwidth=500, stretch=NO)
        self.tree_eventos.heading('#8', text='ROA')

        self.tree_eventos.column("column9", width=60, minwidth=500, stretch=NO)
        self.tree_eventos.heading('#9', text='ROIC')

        self.tree_eventos.column("column10", width=60, minwidth=500, stretch=NO)
        self.tree_eventos.heading('#10', text='BETA')

        self.tree_eventos.grid(row=0, column=3, padx=10, pady=10, columnspan=3, rowspan=10)

        self.ver_compromissos_backEnd()
        self.contabil.mainloop()

    def ver_compromissos_backEnd(self):
        # Aqui é onde tratamos os dados para plotar eles

        dados = pd.read_csv('statusinvest-busca-avancada.csv', decimal=',', thousands='.', sep = ';')

        self.tree_eventos.delete(*self.tree_eventos.get_children())

        #acoes = ['ITUB4']
        acoes = list(self.pegando_dados_acoes)

        colunas = ['TICKER', 'PRECO', 'P/L', 'DY', 'P/VP', 'EV/EBIT', 'ROE', 'ROA', 'ROIC']

        dados = dados[colunas]

        cont = 0
        lista_dados_cont = list()
        teste = list()

        for a in dados.values:

            if a[0] in acoes:
                lista_dados_cont.append(list(a))
            else:
                continue

            teste.append(lista_dados_cont)
            lista_dados_cont = list()

        for a in range(len(teste)):
            (teste[a][0].append(list(inv.get_stock_information(acoes[a], 'BRAZIL')['Beta'].values)[0]))

        for linha in teste:
            self.tree_eventos.insert('', END, values=linha[0])


Janela_Dashboard()




