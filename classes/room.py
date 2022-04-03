class Room:
    def __init__(self, name, capacity, fee):
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.patrons = []
