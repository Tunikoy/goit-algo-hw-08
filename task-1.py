import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізація мінімальної купи
    heapq.heapify(cables)
    
    total_cost = 0

    # Поки більше одного кабелю в купі
    while len(cables) > 1:
        # Виймаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх
        cost = first + second
        total_cost += cost

        # Додаємо результат назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
