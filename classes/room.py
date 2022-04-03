class Room:
    def __init__(self, number, capacity, fee, playlist):
        self.number = number
        self.capacity = capacity
        self.fee = fee
        self.playlist = playlist
        self.patrons = []
    
    def check_in(self, group):
        self.patrons += group
