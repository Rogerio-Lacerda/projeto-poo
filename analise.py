import pandas as pd

class AnaliseInicial:
    def __init__(self, tabela):
        self.dataFrame = tabela

    def qtdElementos(self):
        quantidade = self.dataFrame["Total"].count()
        return quantidade

    def tipoColunas(self):
        self.dataFrame["Data"] = pd.to_datetime(self.dataFrame["Data"])
        colunas = self.dataFrame.dtypes
        return colunas