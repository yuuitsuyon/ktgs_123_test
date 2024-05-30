# Расчет количества книг на дискете

BYTES_ONE_CHARS = 4
volume= 1.44
pages = 100
lines = 50
chars = 25

total_chars = pages * lines * chars
book_volume = total_chars * BYTES_ONE_CHARS

disk_volume = volume * 1024 * 1024
numbers_book = disk_volume // book_volume
print('Количество книг на дискете:', numbers_book)

# Арифмитические операторы и избегание магических чисел

length = 90
width = 50
perimetr = length + length + width + width
print('Периметр футбольного поля:', perimetr)


# Расчет периметра и площади геометрических фигур

radius = 5
side = 5
pi = 3.1415
print('Периметр:', round (perimetr,2))



