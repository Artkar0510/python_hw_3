purchases = {}

with open('purchase_log.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        user_id, category = line.split(' ', 1)
        category = category.replace('‘', '').replace('’', '')
        purchases[user_id] = category

print('Первые два элемента purchases:')
i = 0
for k, v in purchases.items():
    print(k, v)
    i += 1
    if i == 2:
        break
