# ANALİZ METODU ------------------------------------
from typing import List, Tuple

def select_max_dynamic_limit_fixed(data: List[str], start_limit: int = 12) -> List[List[int]]:
    """
    Her satır için soldan sağa tarama yapar ve sondan limit kadar basamağı
    tarayarak en büyük rakamları seçer.
    """
    lines = data[0].strip().splitlines()
    all_selected = []

    for line in lines:
        digits = [int(c) for c in line.strip()]
        n = len(digits)
        selected = []
        pozisyon = 0
        limit = start_limit

        while limit > 0 and pozisyon < n:
            # Tarama pencere sonu: n - (limit - 1)
            tarama_sonu = n - (limit - 1)
            # Tarama pencere başlangıcı: mevcut pozisyon
            tarama_basi = pozisyon
            pencere = digits[tarama_basi:tarama_sonu]

            if not pencere:
                break

            # Pencere içindeki en büyük rakam ve pozisyonu
            max_val = max(pencere)
            max_idx = pencere.index(max_val) + tarama_basi

            # Kaydet
            selected.append(max_val)

            # Pozisyonu güncelle
            pozisyon = max_idx + 1

            # Limit azalt
            limit -= 1

        all_selected.append(selected)

    return all_selected

# --------------------------------------------------
# SAYISALLAŞTIRMA METODU ---------------------------

def convert_lists_to_numbers_list(data: List[List[int]]) -> List[Tuple[int, ...]]:
    """
    Her alt listeyi birleştirip bir sayı haline getirir ve tümünü tek bir tuple olarak,
    liste içinde döner.
    """
    result = []

    for lst in data:
        num_str = ''.join(str(d) for d in lst)
        num = int(num_str)
        result.append(num)

    return [tuple(result)]


# --------------------------------------------------
# TOPLAMA METODU -----------------------------------

def sum_numbers(data):
    """
    Input örneği: [(98, 99, 87, 92)]
    İçindeki tüm sayıların toplamını döner.
    """
    if not data or not isinstance(data[0], tuple):
        raise ValueError("Input [(...)] formatında olmalı.")

    return sum(data[0])


# --------------------------------------------------
# MAİN CODE ----------------------------------------

data = ["""
987654321111111
811111111111119
234234234234278
818181911112111
"""]

print(select_max_dynamic_limit_fixed(data))
print(convert_lists_to_numbers_list(select_max_dynamic_limit_fixed(data)))
print(sum_numbers(convert_lists_to_numbers_list(select_max_dynamic_limit_fixed(data))))
