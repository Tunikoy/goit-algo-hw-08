import heapq

def merge_k_lists(lists):
    min_heap = []
    
    # Додаємо перші елементи кожного списку в купу
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))  # (значення, індекс списку, індекс елемента)

    merged_list = []

    # Об'єднуємо всі списки
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)

        # Додаємо наступний елемент зі списку в купу
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))

    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
