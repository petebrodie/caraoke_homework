class Room:

    def __init__(self, room_number):
        self.room_number = room_number
        self.guests = []
        self.songs = []


# can add song
    def can_add_song(self,song):
        self.songs.append(song)

#can add guest
    def can_add_guest(self, guest):
        self.guests.append(guest)


# can remove guest
    def can_remove_guest(self, guest):
        self.guests.remove(guest)
