class Guest:
    def __init__(self, name, fav_song = None):
        self.name = name
        self.fav_song = fav_song
        self.cash = 0

    def lift_cash(self, transact):
        self.cash += transact
    
    def celebrate(self, playlist = None):
        if playlist != None:
            if self.fav_song in playlist:
                return "YAAAAAAASSSSS!"
            else:
                return "Aww..."
    
    def check_balance(self, price):
        return self.cash >= price
    
    def spend_money(self, price):
        if self.check_balance(price):
            self.cash -= price
            return price
