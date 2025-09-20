from datetime import datetime
import time

while True:
    # Отримуємо поточну дату і час
    now = datetime.now()
    
    # Форматуємо дату і час
    current_date = now.strftime("%d.%m.%Y")  # Формат: ДД.ММ.РРРР
    current_time = now.strftime("%H:%M:%S")  # Формат: ГГ:ХХ:СС
    
    # Виводимо дату і час
    print(f"Дата: {current_date} | Час: {current_time}")
    
    # Оновлюємо кожну секунду
    time.sleep(1)
    
    # Очищаємо консоль (працює в Windows, для Linux/Mac використовуйте 'clear')
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
