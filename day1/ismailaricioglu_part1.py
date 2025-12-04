class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        new = Node(value)

        if self.head is None:
            # İlk eleman kendine bağlanır
            self.head = new
            new.next = new
            new.prev = new
        else:
            tail = self.head.prev

            tail.next = new
            new.prev = tail

            new.next = self.head
            self.head.prev = new

        self._size += 1

    def go_forward(self, node):
        return node.next

    def go_backward(self, node):
        return node.prev

    def find(self, value):
        cur = self.head
        for _ in range(self._size):
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def to_list(self, limit=None):
        """Döngüsel olduğu için limit verilmezse tüm listeyi bir tur döner."""
        if self.head is None:
            return []

        result = []
        cur = self.head
        count = 0
        limit = limit or self._size

        while count < limit:
            result.append(cur.value)
            cur = cur.next
            count += 1

        return result

# ---

dll = CircularDoublyLinkedList()

# 0-99 arası dolduralım
for i in range(100):
    dll.append(i)

node_99 = dll.find(99)
node_0 = dll.find(0)

print(node_99.next.value)   # 0
print(node_0.prev.value)    # 99

# ---------------------------------------------
# Başlangıç node'u
position_node = dll.find(50)
zero_count = 0

# Örnek kod listesi: "R" ileri, "L" geri
data = """
L1
R2
"""
codes = data.split()


def parse_code(code):
    """Harfi ve sayıyı ayırır"""
    return code[0], int(code[1:])

for code in codes:
    direction, number = parse_code(code)

    for _ in range(number):
        if direction == "R":
            position_node = dll.go_forward(position_node)
        else:
            position_node = dll.go_backward(position_node)

    if position_node.value == 0:
        zero_count += 1

    #print(f"{code}: pozisyon -> {position_node.value}")

print("0 dan geçiş sayısı:", zero_count)
