import csv


def analyze_log(path_to_file):
    file = path_to_file.split('.')[-1]
    if file != 'csv':
        raise FileNotFoundError(
            f'No such file or directory: \'{path_to_file}\'')
    else:
        maria = most_requested_dish_maria(path_to_file)
        arnaldo = hamburguer_order_arnaldo(path_to_file)
        joao = dishes_not_ordered_joao(path_to_file)
        joao_days = days_not_present_joao(path_to_file)
        results = [maria, arnaldo, joao, joao_days]

        with open('data/mkt_campaign.txt', 'w') as f:
            for result in results:
                f.write(str(result) + '\n')


def most_requested_dish_maria(log_file):
    dish_count = {}
    with open(log_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == 'maria':
                if row[1] in dish_count:
                    dish_count[row[1]] += 1
                else:
                    dish_count[row[1]] = 1
    return max(dish_count, key=dish_count.get)


def hamburguer_order_arnaldo(log_file):
    order = 0
    with open(log_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == 'arnaldo':
                if row[1] == 'hamburguer':
                    order += 1
    return order


def dishes_not_ordered_joao(log_file):
    orders = set()
    order_joao = set()
    with open(log_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            orders.add(row[1])
            if row[0] == 'joao':
                order_joao.add(row[1])
    dishes_not_ordered = orders - order_joao
    return dishes_not_ordered


def days_not_present_joao(log_file):
    days = set()
    days_present = set()
    with open(log_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            days.add(row[2])
            if row[0] == 'joao':
                days_present.add(row[2])
    days_not_present = days - days_present
    return days_not_present
