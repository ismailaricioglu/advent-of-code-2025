# --------------------------------------------------
# Aralıkları ve ID listesini ayırma
def split_ranges(text: str):
    """
    Verilen metni satır satır okuyarak, boş satıra kadar olan tüm aralıkları (range)
    listeleyen fonksiyon. Boş satır görüldüğünde ID bölümüne geçildiği varsayılır,
    bu fonksiyon ise yalnızca aralık kısmıyla ilgilenir.
    """
    ranges = []
    lines = text.splitlines()
    
    blank_found = False
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            blank_found = True
            continue
        if not blank_found:
            ranges.append(stripped)
    
    return ranges

# --------------------------------------------------
# Aralıkları birleştirip null-null ekleyen hafıza dostu fonksiyon
def generate_interval_tree(data: str):
    """
    Aralıkları okuyup sıralayan ve çakışan/bitişik aralıkları birleştiren fonksiyon.
    Eğer iki aralık arasında boşluk varsa, bunu göstermek için araya "null-null"
    ekler. Daha hafif bellek kullanımı için doğrudan birleştirilmiş aralık listesi
    """
    input_ranges = split_ranges(data)
    
    # Aralıkları tuple listesine çevir ve başlangıca göre sırala
    intervals = []
    for r in input_ranges:
        start, end = map(int, r.split('-'))
        intervals.append((start, end))
    intervals.sort(key=lambda x: x[0])

    result = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end + 1:
            # Aralıklar birbirine bitişik veya çakışıyor, birleştir
            current_end = max(current_end, end)
        else:
            # Aralıklar arasında boşluk var
            result.append(f"{current_start}-{current_end}")
            result.append("null-null")
            current_start, current_end = start, end

    # Son aralığı ekle
    result.append(f"{current_start}-{current_end}")
    
    return result

# --------------------------------------------------
# 2. sorunun cevabı tezelerin sayısı ---------------
def total_range_count(data: str):
    """
    Birleştirilmiş aralık listesini alır, "null-null" girişlerini yok sayarak
    gerçek aralıkların toplam uzunluğunu hesaplar. Her aralığın hem başlangıç hem
    bitiş değerleri dahil edilerek toplam tez sayısı bulunur.
    """
    ranges_list = generate_interval_tree(data)
    total = 0
    for r in ranges_list:
        if r == "null-null":
            continue
        start, end = map(int, r.split('-'))
        total += end - start + 1  # baş ve son dahil
    return total

# --------------------------------------------------
# MAİN CODE ----------------------------------------

data = """3-5
10-14
16-20
12-18
12-22

1
5
8
11
17
32
"""

print(f"2. sorunun cevabı tezelerin sayısı: {total_range_count(data)}")
