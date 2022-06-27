"""
Desenvolva um programa que deve ler um arquivo csv intitulado
“notas_alunos.csv”
. O arquivo deve ter a seguinte estrutura:

aluno: Nome do aluno;
nota_1: Primeira nota;
nota_2: Segunda nota;
faltas: Número de faltas;

O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

Por fim, o programa deverá mostrar na tela:
- o maior número de faltas;
- a média geral das notas dos alunos;
- e a maior média.

"""
import pandas as pd

tb = pd.read_csv("notas_alunos.csv")
media = (tb["Primeira_nota"] + tb["Segunda_nota"]) / 2
tb["media"] = media
tb["situação"] = ""

tb.loc[tb["media"] >= 7, "situação"] = "APROVADO"
tb.loc[tb["media"] < 7, "situação"] = "REPROVADO"
tb.loc[tb["Numero_de_faltas"] > 5, "situação"] = "REPROVADO"
print(tb)

maior_faltas = tb["Numero_de_faltas"].max()
print(f"\nO Maior Numero de Faltas: {maior_faltas}")

media_geral = tb["media"].median()
print(f"A média geral das notas dos alunos: {media_geral}")

maior_media = tb["media"].max()
print(f"A maior média : {maior_media}")