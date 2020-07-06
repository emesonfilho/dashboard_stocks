import investpy as inv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

class Historical_data:
    def __init__(self, data_inicial, data_final, pais='brazil', json=False, ordem='ascending', intervalo='Daily'):
        """
        :param data_inicial: data de início da amostra
        :param data_final: data de início da amostra
        :param pais: de qual pais tu quer pegar os dados
        :param json: se quer em json ou não
        :param ordem: asc ou desc
        :param intervalo: intervalo dos dados
        """


        self.data_inicial = data_inicial
        self.data_final = data_final
        self.pais = pais
        self.json = json
        self.ordem = ordem
        self.intervalo = intervalo

    def historico_acoes(self, acao, status='Close'):

        """
        :param acao: acao que tu quer pegar (mesmo sendo só uma, deve ser passada como lista)
        :param status: Pode ser Close / Open / Low / High / Volume / Currency
        :return: retorno dos dados
        """

        if len(acao) > 1:
            dados = pd.DataFrame()
            for papel in acao:
                dados[papel] = inv.get_stock_historical_data(papel, self.pais,
                                                             from_date=self.data_inicial,
                                                             to_date=self.data_final,
                                                             as_json=False,
                                                             order=self.ordem,
                                                             interval=self.intervalo)[status]
            if self.json:
                data = dict()
                for colunas in dados.columns:
                    paper = list()
                    for infos in range(len(dados)):
                        paper.append({
                            "data": dados.index[infos].strftime("%Y-%m-%d"),
                            "preço": dados[colunas][infos]
                        })
                    data[colunas] = paper
                return data

            else:
                return dados

                # to_json -> json.dumps(limpando, ensure_ascii=False).encode('utf8')

        else:
            dados = pd.DataFrame()
            for papel in acao:
                dados = inv.get_stock_historical_data(papel, self.pais,
                                                      from_date=self.data_inicial,
                                                      to_date=self.data_final,
                                                      as_json=False,
                                                      order=self.ordem,
                                                      interval=self.intervalo)
            if self.json:
                stock_json = dict()
                dados['Date'] = dados.index.strftime("%Y-%m-%d")
                stock_json[acao[0]] = dados.to_dict('records')
                return stock_json
            else:
                return dados

    def historico_index(self, indice, status='Close'):
        """
        :param indice: índice que deseja analisar
        :param status: Pode ser Close / Open / Low / High / Volume / Currency /
        :return: Retorno dos dados
        """
        if len(indice) > 1:
            dados = pd.DataFrame()
            for papel in indice:
                dados[papel] = inv.get_index_historical_data(papel, self.pais,
                                                             from_date=self.data_inicial,
                                                             to_date=self.data_final,
                                                             as_json=False,
                                                             order=self.ordem,
                                                             interval=self.intervalo)[status]
            if self.json:
                data = dict()
                for colunas in dados.columns:
                    paper = list()
                    for infos in range(len(dados)):
                        paper.append({
                            "data": dados.index[infos].strftime("%Y-%m-%d"),
                            "preço": dados[colunas][infos]
                        })
                    data[colunas] = paper
                return data

            else:
                return dados

                # to_json -> json.dumps(limpando, ensure_ascii=False).encode('utf8')

        else:
            dados = pd.DataFrame()
            for papel in indice:
                dados = inv.get_index_historical_data(papel, self.pais,
                                                      from_date=self.data_inicial,
                                                      to_date=self.data_final,
                                                      as_json=False,
                                                      order=self.ordem,
                                                      interval=self.intervalo)
            if self.json:
                stock_json = dict()
                dados['Date'] = dados.index.strftime("%Y-%m-%d")
                stock_json[indice[0]] = dados.to_dict('records')
                return stock_json
            else:
                return dados

    def filtro_papeis(self, ordenar='P/L', ranking=False):
        """
        :param ordenar: Indicador que você deseja usar para organizar os dados
        :param ranking: True = menor para o maior | False = maior para o menor
        :return: Retorna os dados
        """
        url = 'https://www.fundamentus.com.br/resultado.php'
        dados = pd.read_html(url, decimal=',', thousands='.')[0]

        for coluna in ['Div.Yield', 'Mrg Ebit', 'Mrg. Líq.', 'ROIC', 'ROE', 'Cresc. Rec.5a']:
            dados[coluna] = dados[coluna].str.replace('.', '')
            dados[coluna] = dados[coluna].str.replace(',', '.')
            dados[coluna] = dados[coluna].str.rstrip('%').astype('float') / 100

        dados = dados.sort_values(ordenar, ascending=ranking)

        if self.json:
            stock_json = dict()
            dados['Date'] = dados.index
            stock_json['contabilidade'] = dados.to_dict('records')
            return stock_json
        else:
            return dados

