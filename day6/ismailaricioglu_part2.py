# --------------------------------------------------------------
# 6. Sorunun 2. Bölümünü Çözer
# --------------------------------------------------------------
# Temel mantık:
#   • Sütunlar sağdan sola okunur.
#   • Her sütun, yukarıdan aşağıya yazılmış bir sayıdır.
#   • Sütun grupları, arada tamamen boş bir kolon varsa ayrılır.
#   • En alt satırdaki sembol o problem için kullanılacak operatördür.
#
# Örnek:
#   123 328  51 64 
#    45 64  387 23 
#     6 98  215 314
#   *   +   *   +
#
# Sağdan sola 4 grup vardır.
# --------------------------------------------------------------

from functools import reduce
import operator

# --------------------------------------------------------------
# Tek bir problemi işle
# --------------------------------------------------------------
def eval_problem(numbers, op):
    """
    numbers: solve_from_text tarafından üretilen sayılar listesi
    op: '+', '*', '-', '/'
    
    Açıklama:
      '+' -> tüm sayıların toplamı
      '*' -> hepsinin çarpımı
      '-' -> soldan sağa sırayla çıkarma (n0 - n1 - n2 ...)
      '/' -> soldan sağa sırayla tam sayı bölme (0 tabanlı, truncate)
    """
    if op == '+':
        return sum(numbers)

    if op == '*':
        return reduce(operator.mul, numbers, 1)

    if op == '-':
        return reduce(lambda a, b: a - b, numbers)

    if op == '/':
        def div(a, b):
            if b == 0:
                raise ZeroDivisionError("Bölme işleminde bölünen 0 olamaz.")
            return int(a / b)  # truncate toward zero
        return reduce(div, numbers)

    raise ValueError(f"Tanınmayan operatör: {op}")

# --------------------------------------------------------------
# Ana çözüm fonksiyonu
# --------------------------------------------------------------
def solve_from_text(text):
    """
    6. Sorunun 2. Bölümünün tamamını çözer.

    Dönen:
        (grand_total, problem_sonuclari)
    """
    lines = text.splitlines()

    # Boş tamamen boş satırları sondan temizle
    while lines and lines[-1].strip() == "" and all(ch == " " for ch in lines[-1]):
        lines.pop()

    if not lines:
        return 0, []

    # Tüm satırları aynı genişliğe pad et
    maxw = max(len(line) for line in lines)              		            # Tüm satırlar içinde en uzun satır genişliğini bul.
    rows = [line.ljust(maxw) for line in lines]          		            # Tüm satırları bu genişliğe göre sağa boşluk ekleyerek hizala.
    
    operator_row_index = len(rows) - 1                   		            # En alttaki satırın (operatör satırı) indeksini al.
    num_rows = operator_row_index                        		            # Operatör satırından önceki satır sayısını belirle.
    
    # Ayrıştırılabilir sütunlar (herhangi bir satırda boş olmayan karakter var mı)
    non_separator = [
        any(rows[r][c] != " " for r in range(len(rows))) 		            # Bu sütunda en az bir hücre boş değilse True olarak işaretle.
        for c in range(maxw)                             		            # Tüm sütunları kontrol et.
    ]
    
    # Boş olmayan sütun kümelerini (bloklarını) tespit et
    spans = []
    c = 0
    while c < maxw:                                                     # Sütunları soldan sağa dolaş.
        if not non_separator[c]:                         	 	            # Bu sütun tamamen boşsa geç.
            c += 1
            continue
        start = c                                         		          # Dolgun blok başlangıcını işaretle.
        while c + 1 < maxw and non_separator[c + 1]:      		          # Bir sonraki sütun da boş değilse bloğu genişlet.
            c += 1
        end = c                                           		          # Bloğun bittiği sütunu işaretle.
        spans.append((start, end))                        		          # Bulunan blok aralığını listeye ekle.
        c += 1                                            		          # Sonraki sütundan devam et.
    
    problem_results = []                                  		          # Her problem için hesaplanan sonuçların tutulacağı liste.


    # ----------------------------------------------------------
    # Her blok bir problem
    # ----------------------------------------------------------
    for start, end in spans:                                            # Her sütun bloğunu (bir problemi) sırayla işle.
        op_char = rows[operator_row_index][end]                         # Operatörü bloğun en sağ sütunundan almaya çalış.
        if op_char == " ":                                              # Eğer o hücre boşsa operatörü bulmak için geriye doğru tara.
            found = False
            for cc in range(end, start - 1, -1):                        # Sağdan sola, blok içinde dolaş.
                if rows[operator_row_index][cc].strip():                # Boş olmayan bir karakter bulunduysa o operatördür.
                    op_char = rows[operator_row_index][cc]
                    found = True
                    break
            if not found:                                               # Hiç operatör bulunamadıysa hata fırlat.
                raise ValueError(f"{start}-{end} bloğunda operatör yok.")
    
        columns = list(range(start, end + 1))[::-1]                     # Sütunları sağdan sola olacak şekilde sırala.
    
        numbers = []                                                    # Bu problemdeki sayıları saklamak için liste.
    
        for cc in columns:                                              # Her sütunu teker teker işle.
            chars = ''.join(rows[r][cc] for r in range(num_rows))       # O sütundaki tüm satırları yukarıdan aşağıya birleştir.
            digits = chars.replace(' ', '')                             # Boşlukları silip gerçek rakam dizisini elde et.
    
            if digits == "":                                            # Eğer tamamen boş sütunsa atla.
                continue
    
            try:
                numbers.append(int(digits))                             # Rakam dizisini tam sayı olarak listeye ekle.
            except:
                raise ValueError(f"{cc}. sütundan sayı okunamadı: '{digits}'")
    
        if not numbers:                                                 # Bu blokta hiç sayı yoksa problemi es geç.
            continue
    
        result = eval_problem(numbers, op_char)                         # Sayıları operatöre göre işleyip sonucu hesapla.
        problem_results.append(result)                                  # Bulunan sonucu sonuç listesine ekle.
    
    grand_total = sum(problem_results)                                  # Tüm problem sonuçlarını toplayarak genel toplamı bul.
    return grand_total, problem_results                                 # Hem büyük toplamı hem de tek tek sonuçları döndür.



# --------------------------------------------------------------
# Örnek test (istenirse)
# --------------------------------------------------------------
if __name__ == "__main__":
    data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    total, results = solve_from_text(data)
    #print("Problemlerin sonuçları:", results)
    print("Grand Total:", total)
