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
def faturacao_mensal(vendas: list[dict]) -> dict:
    """Devolve um dicionário {'AAAA-MM': faturacao} ordenado por mês."""
    por_mes = {}
    for venda in vendas:
        mes = venda["data"][:7]
        valor = total_venda(venda)
        por_mes[mes] = por_mes.get(mes, 0) + valor
    return dict(sorted(por_mes.items()))
def formatar_cve(valor: int) -> str:
    """Formata um valor inteiro com espaços nos milhares e sufixo CVE."""
    formatado = f"{valor:,}".replace(",", " ")
    return f"{formatado} CVE"
def main() -> None:
    caminho = sys.argv[1] if len(sys.argv) > 1 else "data/vendas_amostra.csv"
    vendas = ler_vendas(caminho)
    total = faturacao_total(vendas)
    por_ilha = faturacao_por_ilha(vendas)
    por_mes = faturacao_mensal(vendas)
    top = ilha_top(por_ilha)

    print(f"Total de vendas: {len(vendas)}")
    print(f"Faturação total: {formatar_cve(total)}")
    print(f"Ilha com maior faturação: {top}")
    print("\nFaturação por ilha:")
    for ilha, valor in por_ilha.items():
        print(f"  - {ilha}: {formatar_cve(valor)}")
    print("\nFaturação por mês:")
    for mes, valor in por_mes.items():
        print(f"  - {mes}: {formatar_cve(valor)}")

