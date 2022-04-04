from classes.guest import Guest

class Room:
    def __init__(self, number, capacity, fee, playlist):
        self.number = number
        self.capacity = capacity
        self.fee = fee
        self.takings = 0
        self.playlist = playlist
        self.patrons = []
    
    def take_money(self, transact):
        self.takings += transact
    
    def admit_guests(self, group):
        return [guest for guest in group if Guest.check_balance(guest, self.fee)]

    def collect_fees(self, group):
        for guest in group:
            self.take_money(Guest.spend_money(guest, self.fee))
    
    def check_in(self, group):
        if len(self.admit_guests(group)) != 0:
            self.collect_fees(self.admit_guests(group))
            self.patrons += self.admit_guests(group)
    
    def add_song(self, song):
        self.playlist.append(song)
