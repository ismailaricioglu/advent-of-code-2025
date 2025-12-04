# FORMATLAMA ---------------------------------------

# Girilen sayıların başındaki 0 kaldırılır
def remove_leading_zeros_str(n: str) -> str:
    """
    Girilen string sayıdaki baştaki 0'ları kaldırır.
    Örnek: '00123' -> '123'
    """
    return n.lstrip('0') or '0'
    
#print(remove_leading_zeros_str("00123"))   # '123'
#print(remove_leading_zeros_str("0000"))    # '0'
#print(remove_leading_zeros_str("0456"))    # '456'

# İnput verisini formatlama
def parse_range_input(text: str):
    """
    '011-022,95-115,998-1012,...' gibi bir metni
    [('11', '22'), ('95', '115'), ...] şeklinde bir listeye çevirir.
    """
    result = []
    parts = text.split(",")
    
    for p in parts:
        p = p.strip()  # boşlukları temizle
        if not p:
            continue
        start, end = p.split("-")
        #result.append((start, end))
        start = remove_leading_zeros_str(start)
        end = remove_leading_zeros_str(end)
        result.append((remove_leading_zeros_str(start), remove_leading_zeros_str(end)))
    
    return result

#input_text = "11-22,95-115,998-1012,1188511880-1188511890"
#ranges = parse_range_input(input_text)
#print(ranges)

# --------------------------------------------------

# MANTIK -------------------------------------------

# Girilen sayının basamakları için ÇİFT/Tek Kontrolü
def is_digit_count_even(n: int) -> bool:
    """
    Girilen sayının basamak sayısı çift mi kontrol eder.
    Çift ise True, tek ise False döner.
    """
    digit_count = len(str(abs(n)))  # negatif sayıları da düzgün ele almak için abs kullanıyoruz
    return digit_count % 2 == 0

#print(is_digit_count_even(1234))   # True
#print(is_digit_count_even(123))    # False
#print(is_digit_count_even(-5678))  # True

# Girilen sayının basamaklarının 2 farklı değişkene atanması
def split_number_into_two_parts(n: int):
    """
    Girilen sayının basamaklarını iki eşit parçaya böler.
    İlk yarıyı ve ikinci yarıyı ayrı değişkenler olarak döndürür.
    """
    s = str(abs(n))  # negatifler için güvenlik
    mid = len(s) // 2
    part1 = int(s[:mid])
    part2 = int(s[mid:])
    return part1, part2

#a, b = split_number_into_two_parts(1188511885)
#print(a)  # '11885'
#print(b)  # '11885'

# Tekrar koşullarını sağlayan tekrarlı sayıların toplamı
def control_ranges(ranges):
    """
    [('11', '22'), ('95', '115'), ...] formatındaki listeyi
    kontrol ederek şartları sağlayan değerlerin toplamını döner
    """
    result = 0
    for start, end in ranges:
        for i in range(int(start), int(end)+1):
            if is_digit_count_even(i):
                a, b = split_number_into_two_parts(i)
                if a == b:
                    #print(a,b)
                    result += i
    print( result)

#ranges = [('11', '22'), ('95', '115'), ('998', '1012'), ('1188511880', '1188511890')]
#control_ranges(ranges)

# --------------------------------------------------

# MAİN CODE ----------------------------------------

# İnput verisini formatlama
input_text = ""
ranges = parse_range_input(input_text)
#print(ranges)
control_ranges(ranges)

# --------------------------------------------------
