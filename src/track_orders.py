class TrackOrders:
    def __init__(self):
        self.ordes = []

    def __len__(self):
        return len(self.ordes)

    def add_new_order(self, costumer, order, day):
        self.ordes.append((costumer, order, day))
        return self.ordes

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
