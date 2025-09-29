class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address  # тип данных Address
        self.from_address = from_address  # тип данных Address
        self.cost = cost  # тип данных число
        self.track = track  # тип данных строка