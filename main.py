from tqdm import tqdm
import time

# Sonlar o'sishini kuzatish
for i in tqdm(range(1, 1001), desc="Sonlar o'sishi", ncols=100, position=0):
    # Agar son 10000 ga bo'lsa, chiqarish
    if i % 10000 == 0:
        print(i)
    time.sleep(0.01)  # Vaqtni kechiktirish (jarayonni sekinlashtirish uchun)
