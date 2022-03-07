class TrackOrders:
    def __init__(self):
        self.ordes = []

    def __len__(self):
        return len(self.ordes)

    def add_new_order(self, costumer, order, day):
        self.ordes.append((costumer, order, day))
        return self.ordes

    def get_most_ordered_dish_per_costumer(self, costumer):
        self.costumer = costumer
        self.dish_count = {}
        for costumer, order, day in self.ordes:
            if costumer == self.costumer:
                if order in self.dish_count:
                    self.dish_count[order] += 1
                else:
                    self.dish_count[order] = 1
        return max(self.dish_count, key=self.dish_count.get)

    def get_never_ordered_per_costumer(self, costumer):
        self.costumer = costumer
        self.orders = set()
        self.orders_ordered = set()
        for costumer, order, day in self.ordes:
            self.orders.add(order)
            if costumer == self.costumer:
                self.orders_ordered.add(order)
        self.dishes_not_ordered = self.orders - self.orders_ordered
        return self.dishes_not_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        self.costumer = costumer
        self.days = set()
        self.days_present = set()
        for costumer, order, day in self.ordes:
            self.days.add(day)
            if costumer == self.costumer:
                self.days_present.add(day)
        self.days_not_present = self.days - self.days_present
        return self.days_not_present

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
