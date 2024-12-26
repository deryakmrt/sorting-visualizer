# Bubble Sort algoritmasi
def bubble_sort(data):
    n = len(data)  # Listenin uzunlugu
    steps = []  # Her adimda listenin durumunu kaydetmek icin bir liste
    # Tum elemanlari siralamak icin dis dongu
    for i in range(n):  
        # Siralanmamis kismi karsilastirmak icin ic dongu
        for j in range(0, n - i - 1):  
            # Yan yana bulunan elemanlari karsilastir
            if data[j] > data[j + 1]:  # Eger soldaki eleman, sagdakinden buyukse:
                data[j], data[j + 1] = data[j + 1], data[j]  # Elemanlarin yerlerini degistir
            steps.append(data.copy())  
    return steps

# Insertion Sort algoritmasi
def insertion_sort(data):
    steps = []
    for i in range(1, len(data)):  # Listenin ikinci elemanindan itibaren dongu baslar
        key = data[i]  # su an siralanmakta olan eleman (anahtar)
        j = i - 1  # Sirali alt listenin son elemaninin indisi
        # Sirali alt listeyi tarayarak, 'key' icin dogru yeri bul
        while j >= 0 and key < data[j]:  # 'key', solundaki elemandan(j) kucukse:
            data[j + 1] = data[j]  # Daha buyuk olan elemani bir adim saga kaydir
            j -= 1  # Bir onceki elemani (daha sola) kontrol et
        # 'key', sirali alt listede dogru yerine yerlestirilir
        data[j + 1] = key  
        steps.append(data.copy())  # O anki listenin durumunu kaydet (animasyon icin)
    return steps  # Tum adimlari dondur (animasyon icin kullanilir)

# Selection Sort algoritmasi
def selection_sort(data):
    steps = []
    n = len(data)
    for i in range(n):
        min_idx = i  # Baslangicta minimum elemanin indeksi
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j  # Daha kucuk bir eleman bulundu
        data[i], data[min_idx] = data[min_idx], data[i]  # Elemanlari takas et
        steps.append(data.copy())  # Her takas sonrasi durumu kaydet
    return steps

# Merge Sort algoritmasi
def merge_sort(data):
    steps = []

    def merge_sort_inner(data, start, end):
        if end - start > 1:
            mid = (start + end) // 2
            merge_sort_inner(data, start, mid)
            merge_sort_inner(data, mid, end)
            merge(data, start, mid, end)

    def merge(data, start, mid, end):
        left = data[start:mid]
        right = data[mid:end]
        k = start
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

        steps.append(data.copy())

    merge_sort_inner(data, 0, len(data))
    return steps

# Heap Sort algoritmasi
def heap_sort(data):
    steps = []
    n = len(data)

    def heapify(data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] > data[largest]:
            largest = left

        if right < n and data[right] > data[largest]:
            largest = right

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            steps.append(data.copy())
            heapify(data, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        steps.append(data.copy())
        heapify(data, i, 0)

    return steps

# Radix Sort algoritmasi
def radix_sort(data):
    steps = []
    max_val = max(data)
    basamak = 1

    while max_val // basamak > 0:
        count_sort(data, basamak)
        basamak *= 10
        steps.append(data.copy())

    return steps

def count_sort(data, basamak):
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = data[i] // basamak
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = data[i] // basamak
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        data[i] = output[i]
