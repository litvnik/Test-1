class Media:
    def play(self):
        return "Playing media"

    def pause(self):
        return "Pausing media"

class Music(Media):
    def play(self):
        return "Playing music track"

class Video(Media):
    def play(self):
        return "Playing video file"