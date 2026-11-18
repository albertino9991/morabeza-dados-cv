"""Resumo das vendas da Morabeza Distribuição (Sessão 1).

Lê um ficheiro CSV de vendas e mostra a faturação total e por ilha.
Só usa a biblioteca padrão do Python: o pandas chega na Sessão 4.
"""

import csv
import sys


def ler_vendas(caminho):
    """Lê o CSV de vendas e devolve uma lista de dicionários, um por venda."""
    vendas = []
    with open(caminho, encoding="utf-8") as ficheiro:
        for linha in csv.DictReader(ficheiro):
            linha["quantidade"] = int(linha["quantidade"])
            linha["preco_unitario"] = int(linha["preco_unitario"])
            vendas.append(linha)
    return vendas


def total_venda(venda: dict) -> int:
    """Valor de uma venda em escudos: quantidade vezes preço unitário."""
    return venda["quantidade"] * venda["preco_unitario"]


def faturacao_total(vendas: list[dict]) -> int:
    """Soma o valor total de todas as vendas."""
    return sum(total_venda(v) for v in vendas)


def faturacao_por_ilha(vendas: list[dict]) -> dict:
    """Calcula a faturação acumulada por cada ilha."""
    por_ilha = {}
    for venda in vendas:
        ilha = venda["ilha"]
        valor = total_venda(venda)
        por_ilha[ilha] = por_ilha.get(ilha, 0) + valor
    return por_ilha


def ilha_top(por_ilha: dict) -> str:
    """Devolve o nome da ilha com maior faturação."""
    return max(por_ilha, key=por_ilha.get)
