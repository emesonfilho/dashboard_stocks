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

class Menu_user:
    def __init__(self, referencia):
        self.meuMenu = Menu(referencia)

        self.confFile()

        referencia.config(menu = self.meuMenu)

    def confFile(self):
        fileMenu = Menu(self.meuMenu, tearoff=0)
        fileMenu.add_command(label='Open')
        self.meuMenu.add_cascade(label='File', menu=fileMenu)


