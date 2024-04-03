from tabela import Tabela
from calculo import Calculos
from grafico import Graficos
from analise import AnaliseInicial

class Program:
    def __init__(self) -> None:
        pass
        
if __name__ == "__main__":

    print("**Configurações da Tabela***")
    caminho_formatar = "import\\projetoPOO.xlsx"
    caminho_leitura = "import\\tabelaPooFormatadaIndice.xlsx"
    configTabela = Tabela(caminho_formatar, caminho_leitura)
    configTabela.formatarExcel()
    dataFrame = configTabela.read()

    grafico = Graficos(dataFrame)
    print("***Retorno dos Gráficos***")
    grafico.distribuicao_normal()
    grafico.getBoxplot()
    grafico.indiceTempo()

    analise =  AnaliseInicial(dataFrame)
    analise.tipoColunas()
    print("***Retorno das Análises***")
    print(f"Qntd de Elementos: {analise.qtdElementos()}")
    print(f"Colunas e Tipos: {analise.tipoColunas()}")

    calculos =  Calculos(dataFrame)
    print("***Retorno dos Cálculos***")
    print(f"Média: {calculos.media()}")
    print(f"Mediana: {calculos.mediana()}")
    print(f"Desvio Padrao: {calculos.desvioPadrao()}")
    print(f"Coeficiente da Variação: {calculos.get_variant_coefficient()}")
    print(f"Valores Quartis: {calculos.quartis()}")