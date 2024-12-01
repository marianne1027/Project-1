import csv
import random
from Track import Track
from PlayList import PlayList

class Queue:
    def __init__(self,size:int=50):
        """Create a Queue"""
        self.queue=[None]*size
        self.size=0
        self.curr = 0
        self.repeat = False
        self.shuffle= True
        self.state=True

    def increaseSize(self):
        """Increase Queue Size"""
        self.size +=1
    def setstate(self,mode):
        if mode == 1:
            self.state=False
        elif mode==2:
            self.state=True

    def getSize(self):
        """Return Queue Size"""
        return self.size

    def enqueue(self,song:Track):
        """Add song to Queue"""
        index=self.size
        self.queue[index]=song
        self.increaseSize()

    
    def listEnqueue(self, list): 
        """Add playlists to queue.
        Reeceive playlists from converted list."""
        for items in list:
            self.enqueue(Track(items[1],items[2],items[3],items[4]))

    def dequeue(self):
        """Remove Song from Queue"""
        if self.size==0:
            return None
        else:
            item=self.queue[0]
            self.queue=self.queue[1:]
            self.size-=1
            return item
        
    # def addtoStorage(self, name): wala ni apil
    #     """Adds the queue into the csv file
    #     Arguments: Name(Set a custom name for the queue)"""
    #     name=[[name]]
    #     manage=open('Library.csv', 'a',newline='')
    #     write= csv.writer(manage)
    #     write.writerows(name,self.convert())

    def getContent(self):
        str=f""
        index=0
        while index < len(self.queue):
            if self.queue[index]==None:
                break
            str+=f"[{self.queue[index]}]\n"
            index+=1
        return str
    
    def convert(self):
        """Convert content into list for storing data into csv file"""
        s=[]
        for items in self.queue:
            if items == None:
                break
            s += [[items]]
        return s
    
    # def convertTime(self): wala ni apil
    #     time=self.duration
    #     minutes, seconds = map(int, time.split(":"))
    #     total_seconds = minutes * 60 + seconds
    #     return total_seconds
    
    def getTotalDuration(self):
        """Returns total duration of the Queue"""
        total_seconds = 0

        for items in self.queue:
            if items is None:
                break
            minutes, seconds = map(int, items.duration.split(":"))
            total_seconds += minutes * 60 + seconds

        total_minutes = total_seconds // 60
        remaining_seconds = total_seconds % 60
        return f"{total_minutes}:{remaining_seconds:02d}"

    def skipTrack(self):
        if self.curr != -1 and self.curr < self.size - 1:
            self.curr += 1
            self.playTrack()
        else:
            if self.repeat:
                self.curr = 0
                self.playTrack()
            else:
                print("No more tracks left.")
                self.curr = -1
                return None
    
    def playTrack(self):
        if self.curr == -1:
            self.curr = 0
        if self.curr < self.size and self.queue[self.curr] is not None:
            print(f"\t{self.queue[self.curr]}")
            print()
            print(f"Next track: {'\n\tNo more tracks left' if self.queue[self.curr+1]==None else self.queue[self.curr+1]}")
        # else:
        #     print(f"No more tracks left.")

    def prevTrack(self):

        if self.curr > 0:
            self.curr -= 1
            self.playTrack()
        else:
            if self.repeat:
                self.curr = self.size - 1
                self.playTrack()
            else:
                self.playTrack()
                self.curr = -1
    
    def showQueue(self):
        if self.size==0:
            print("The queue is empty.")
        else:
            print("<------Songs in Queue------>")
            for i in range(self.size):
                print(f"\n{self.queue[i]}\n")
            print("<---------End of Queue--------->")
            
    def shuffleQueue(self):
        tracks = self.queue[:self.size]
        random.shuffle(tracks)
        self.queue[:self.size] = tracks

    def __str__(self):
        if self.shuffle == True:
            s='Yes'
            self.shuffleQueue()
        s='No'
        if self.repeat==True:
            r='Yes'
        r='No'
        if self.state == False:
            st="(Paused)"
        else:
            st=''
        if self.getSize() !=0:
            q=f'Total Duration: {self.getTotalDuration()}\nShuffled: {s}\tRepeat: {r}\n\
Tracks:\nCurrently Playing {st}:\n\n'
            
            return q
        return 'There is nothing in Queue!\nSelect Playlist.\n'



def loadTracksToQueue(queue):
    with open('Library.csv', mode='r') as storage:
        reader = csv.reader(storage)
        for line in reader:
            if len(line) >= 4:  # Ensure all required data is present
                title, artist, album, duration = line
                track = Track(title, artist, album, duration)
                queue.enqueue(track)
    print(f"Tracks loaded into the queue from Library.csv.\n")
    

p=PlayList()
# print(p.loadplaylist('my playlist'))

# p.addtoPlaylist(p.loadplaylist('my playlist'))
# queue = Queue()
# queue.listEnqueue(p.convert()) 

# print(queue)
# queue.playTrack()
# queue.setstate(1)
# print(queue.player())

#wala ni apil tanan diri
# song1 = Track("Nikes", "Frank Ocean", "Blonde", "5:14")
# song2 = Track("Heartless", "The Weeknd", "After Hours", "3:18")
# song3 = Track("Thinkin Bout You", "Frank Ocean", "Channel Orange", "3:21")
# queue.enqueue(song1)
# queue.enqueue(song2)
# queue.enqueue(song3)
# print(queue)
# print(queue.getTotalDuration())

# queue.toggleRepeat()

# queue.playTrack() #Play 1st song

# queue.skipTrack() #Skip to 2nd song
# # queue.playTrack() #PLay 2nd song

# queue.skipTrack() #Skip to 3rd song
# queue.prevTrack()
# queue.prevTrack()
# queue.skipTrack()
# queue.skipTrack()
# queue.playTrack() #Play 3rd song

# queue.prevTrack() #Go back to 2nd song
# queue.playTrack() #Play 2nd song

# queue.prevTrack() #Go back to 1st song
# queue.playTrack() #Play 1st song

# queue.prevTrack() #Go back to the last song in the queue
# queue.playTrack() #Play last song