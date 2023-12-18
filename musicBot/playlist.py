import random
from collections import deque

from config import config


class Playlist:
    """
    Stores the youtube links of songs to be played and already played and offers basic operation on the queues
    """

    def __init__(self):
        # Stores the links of the songs in queue and the ones already played
        self.playque = deque()
        self.historyque = deque()

        # A seperate history that remembers the names of the tracks that were played
        self.trackname_history = deque()

        self.playinloop = False

    def __len__(self) -> int:
        return len(self.playque)

    def add_name(self, trackname: str) -> None:
        self.trackname_history.append(trackname)
        if len(self.trackname_history) > config.MAX_TRACKNAME_HISTORY_LENGTH:
            self.trackname_history.popleft()

    def add(self, track):
        self.playque.append(track)

    def next(self, song_name) -> str:
        """
        Add song to the play queue
        """
        if self.playinloop == True:
            self.playque.appendleft(self.historyque[-1])

        if len(self.playque) == 0:
            return None

        if song_name != "Dummy":
            if len(self.historyque) > config.MAX_TRACKNAME_HISTORY_LENGTH:
                self.historyque.popleft()

        return self.playque[0]

    def prev(self, current_song) -> str:
        """
        play the previous song
        """
        if current_song is None:
            self.playque.appendleft(self.historyque[-1])
            return self.playque[0]

        idx = self.historyque.index(current_song)
        self.playque.appendleft(self.historyque[idx-1])
        if current_song != None:
            self.playque.insert(1, current_song)

    def shuffle(self):
        random.shuffle(self.playque)

    def move(self, oldidx: int, newidx: int):
        song = self.playque[oldidx]
        del self.playque[oldidx]
        self.playque.insert(newidx, song)

    def empty(self):
        self.playque.clear()
        self.historyque.clear()
