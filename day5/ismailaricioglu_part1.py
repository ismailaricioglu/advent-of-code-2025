# FORMATLAMA ---------------------------------------
def split_ranges_and_ids(text: str):
    """
    Verilen çok satırlı metni iki bölüme ayırır: Üst kısımda aralık (range) değerleri,
    boş satırdan sonraki kısımda ise tam sayı ID'ler bulunur. Bu fonksiyon, boş satırı
    bir ayraç olarak kullanarak önce aralıkları toplar, ardından ID listesini üretir.
    """
    ranges = []
    ids = []
    lines = text.splitlines()
    
    blank_found = False
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            blank_found = True
            continue
        if not blank_found:
            ranges.append(stripped)
        else:
            ids.append(int(stripped))  # Sayıları int olarak alıyoruz
    
    return ranges, ids

# --------------------------------------------------
# KONTROL ------------------------------------------
def check_fresh_list(id_values: list, ranges: list):
    """
    ID listesindeki her değerin verilen aralıklardan hangisine düştüğünü kontrol eder.
    Her ID için "Fresh" veya "Spoiled" durumunu belirleyen bir sözlük döndürür.
    Aralıklar önce (start, end) şeklinde sayısal tuple formatına dönüştürülür.
    """
    # Aralıkları (start, end) tuple listesine çevir
    intervals = []
    for r in ranges:
        start, end = map(int, r.split('-'))
        intervals.append((start, end))
    
    result = {}
    for id_value in id_values:
        status = "Spoiled"
        for start, end in intervals:
            if start <= id_value <= end:
                status = "Fresh"
                break
        result[id_value] = status
    
    return result

# --------------------------------------------------
# 1. sorunun cevabı tezelerin sayısı ---------------

def count_fresh(data: str):
    """
    Verilen veri metnini işleyerek aralık ve ID listelerini çıkarır. Daha sonra
    check_fresh_list fonksiyonuyla ID'lerin durumunu belirler. "Fresh" olan ID
    sayısını hesaplayıp ekrana yazdırır.
    """
    ranges_list, ids_list = split_ranges_and_ids(data)
    #relist = check_fresh_list(ids_list, ranges_list)
    status = check_fresh_list(ids_list, ranges_list)
    fresh_count = sum(1 for status in status.values() if status == "Fresh")
    print(f"1. sorunun cevabı tezelerin sayısı: {fresh_count}")


# --------------------------------------------------
# MAİ CODE -----------------------------------------



data = """3-5
10-14
16-20
12-14

1
5
8
11
17
32
"""

count_fresh(data)
