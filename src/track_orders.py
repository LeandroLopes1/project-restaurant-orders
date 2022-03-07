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
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
