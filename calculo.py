class Calculos:
    def __init__(self, tabela):
        self.tabela = tabela

    def media(self):
        total = self.tabela["Total"]
        media = total.sum() / total.count()
        
        return media
    
    def mediana(self):
        orderTotal = self.tabela.sort_values(by="Total")
        mediana = orderTotal["Total"].median()
        return mediana

    def desvioPadrao(self):
        dpTotal = self.tabela["Total"].std()
        return dpTotal
    
    def get_variant_coefficient(self) -> float:
        """Obtém o coeficiente de variação da planilha."""

        average = self.tabela["Total"].mean()
        default_deviation = self.tabela["Total"].std()

        return default_deviation / average
    
    def quartis(self):
        values_total = self.tabela.sort_values(by="Total")
        quartis = values_total.describe(percentiles=[.25, .5, .75]).loc[['25%', '50%', '75%']]
        q1 = quartis.loc['25%'].iloc[0]
        q2 = quartis.loc['50%'].iloc[0]
        q3 = quartis.loc['75%'].iloc[0]
        quartis_string = f"Q1 = {q1}, Q2 = {q2}, Q3 = {q3}"
        return quartis_string