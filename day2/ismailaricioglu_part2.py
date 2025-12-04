# FORMATLAMA ---------------------------------------

# Girilen sayıların başındaki 0 kaldırılır
def remove_leading_zeros_str(n: str) -> str:
    """
    Girilen string sayıdaki baştaki 0'ları kaldırır.
    Örnek: '00123' -> '123'
    """
    return n.lstrip('0') or '0'
    
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

# --------------------------------------------------

# MANTIK -------------------------------------------

# Girilen sayının basamak sayısının bölenleri
def get_digit_count_divisors(number: int):
    """
    Girilen sayının basamak sayısının bölenlerini listeler.
    Kendi basamak sayısı hariç tutulur.
    Örnek: 123123123 (9 basamak) -> [1, 3]
    """
    digit_count = len(str(abs(number)))
    divisors = [i for i in range(1, digit_count) if digit_count % i == 0]
    return divisors


#number = 123123123
#print(get_digit_count_divisors(number))
# Çıktı: [1, 3, 9] çünkü sayı 9 basamaklı ve 1,3,9 9'u tam böler

# Girilen sayıyı n basamaklı Listesi
def split_number_by_n_list(number: int, n_list: list): 
    """
    Girilen sayıyı n basamaklı parçalarına böler ve sözlük olarak döner.
    
    number: Bölünecek sayı
    n_list: Basamak sayılarının listesi
    Dönen değer: {[parçalar]} sözlüğü
    """
    s = str(abs(number))
    result = {}
    for n in n_list:
        result[n] = [int(s[i:i+n]) for i in range(0, len(s), n)]
    return result

#number = 123123
#n_list = [3, 2]

#splits = split_number_by_n_list(number, n_list)
#print(splits)




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
            splits = split_number_by_n_list(i,get_digit_count_divisors(i))
            """
            splits: {n: [parçalar]} formatındaki sözlük
            Her n için parçaların eşitliğini kontrol eder.
            Eşitse parçayı toplama ekler.
            """
            # Her sayı için bir kez toplamak için flag kullanıyoruz
            added = False
            for parts in splits.values():
                if not added and all(x == parts[0] for x in parts):
                    #print(f"{i} => {parts}")
                    result += i
                    added = True  # Bu sayının tekrar eklenmesini engeller
    return result
    #print( result)

#ranges = [('11', '22'), ('95', '115'), ('998', '1012'), ('1188511880', '1188511890')]
#control_ranges(ranges)

# --------------------------------------------------

# MAİN CODE ----------------------------------------

# İnput verisini formatlama
input_text = ""
ranges = parse_range_input(input_text)
#print(ranges)
print(f"TOPLAM: {control_ranges(ranges)}")


# --------------------------------------------------
