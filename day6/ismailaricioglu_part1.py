# OPERATÖRLERİN LİSTESİ ---------------------------------
def extract_operators(block: str):
    """
    Çok satırlı metnin en alt satırındaki matematik operatörlerini
    liste halinde döndürür.
    Örnek operatörler: +, -, *, /
    """
    lines = [line.strip() for line in block.splitlines() if line.strip()]

    # Son satır operatör satırıdır
    operator_line = lines[-1]

    # Operatörleri ayıklama: harf/sayı olmayan karakterleri seç
    ops = [ch for ch in operator_line if ch in "+-*/"]

    return ops

# ------------------ ÖRNEK KULLANIM ---------------------
#print(extract_operators(data))

# -------------------------------------------------------
# SÜTUN SAYISI ------------------------------------------

def count_operators(block: str):
    """
    Çok satırlı metnin en alt satırındaki matematiksel operatörlerin
    toplam sayısını döndürür.
    Desteklenen operatörler: + - * /
    """
    lines = [line.strip() for line in block.splitlines() if line.strip()]

    # Son satır operatör satırıdır
    operator_line = lines[-1]

    # Operatörleri say
    count = sum(1 for ch in operator_line if ch in "+-*/")

    return count

# ------------------ ÖRNEK KULLANIM ---------------------
#print(count_operators(data))

# -------------------------------------------------------
# SÜTUN'a GÖRE HEAPLA -----------------------------------

import operator

def compute_by_column(block: str, operators: list):
    # Desteklenen işlemler
    op_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    # Sayı satırlarını temizle
    lines = [line.strip() for line in block.splitlines() if line.strip()]
    number_lines = lines[:-1]

    # Matris oluştur
    matrix = [
        [int(n) for n in row.split()]
        for row in number_lines
    ]

    results = []

    for col_idx, op_char in enumerate(operators):
        if op_char not in op_map:
            raise ValueError(f"Bilinmeyen operatör: {op_char}")

        op_func = op_map[op_char]
        column = [row[col_idx] for row in matrix]

        # İlk değer başlangıç
        res = column[0]

        # Kalanları sırayla uygula (otomatik)
        for val in column[1:]:
            res = op_func(res, val)

        results.append(res)

    return results

# ------------------ ÖRNEK KULLANIM ---------------------
#print(compute_by_column(data, extract_operators(data)))

# -------------------------------------------------------
def sum_list(values: list):
    """
    Listenin tüm elemanlarının toplamını döndürür.
    """
    total = 0
    for v in values:
        total += v
    return total
    
# ------------------ ÖRNEK KULLANIM ---------------------
#nums = [33210, 490, 4243455, 401]
#print(sum_list(nums))


# -------------------------------------------------------
# MAİN CODE ---------------------------------------------

data = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   + 
"""
print(extract_operators(data))
print(count_operators(data))
print(compute_by_column(data, extract_operators(data)))
print(sum_list(compute_by_column(data, extract_operators(data))))

