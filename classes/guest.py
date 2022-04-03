class Guest:
    def __init__(self, name, fav_song = None):
        self.name = name
        self.fav_song = fav_song
        self.cash = 0

    def lift_cash(self, transact):
        self.cash += transact
    
    def celebrate(self, playlist = None):
        if playlist != None and self.fav_song in playlist:
            return "YAAAAAAASSSSS!"
