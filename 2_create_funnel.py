purchases = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        user, category = line.strip().split(' ', 1)
        purchases[user] = category

with open('visit_log.csv', 'r', encoding='utf-8') as f_in, \
        open('funnel.csv', 'w', encoding='utf-8') as f_out:
    f_out.write('user_id,source,category\n')
    for line in f_in:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 2: 
            continue
        user_id, source = parts
        if user_id in purchases:
            f_out.write(f'{user_id},{source},{purchases[user_id]}\n')
