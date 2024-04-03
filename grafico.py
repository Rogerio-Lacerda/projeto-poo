import matplotlib.pyplot as plt

class Graficos:
    def __init__(self, tabela):
        self.dataFrame = tabela

    def indiceTempo(self):
        x = self.dataFrame["Data"]
        y = self.dataFrame["Total"]
 
        plt.plot(x, y)
        plt.xticks(rotation=35, ha='right')
        intervalo = 6
        plt.xticks(range(0, len(x), intervalo))
        plt.xlabel('x = Data')
        plt.ylabel('y = Total')
        plt.title("Índice vs Tempo")
        plt.show()
    
    def getBoxplot(self):
        x = self.dataFrame['Total']
        plt.boxplot(x,showfliers=True,flierprops=dict(marker='o',markersize=8,markerfacecolor='red'))
        plt.title("BoxPlot & Outliers")
        plt.show()
    
    def distribuicao_normal(self):
        x = self.dataFrame['Total']
        plt.hist(x,bins=10)
        plt.title("Distribuição Normal dos Índices")
        plt.show()