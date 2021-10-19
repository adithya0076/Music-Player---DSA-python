# KAHDSE202F-001 = kaveesha
# KAHDSE202F-002 = Adithya
# KAHDSE202F-003 = Pasan
# KAHDSE202F-005 = Usitha 
# sadun silva



import array as arr 
class node:
    def __init__(self, playlist):
        self.song = playlist
        self.next = None
        self.prev = None
        print("Song {0} Created".format(self.song))        

   

class LinkedList:
    top = None
    temp = None
    top1 = None

    def __init__(self):
        self.head = None
        self.top = None
        self.tail = None
        print("PlayList Is Created")

    def tofile(self, a):
        songs = a
        print(songs)
        f1 = open("playlist.txt",mode="a+",encoding="utf-8")
        f1.write(songs)
        f1.close()

    def add_node(self):
        print("\n\a\a\a\aEnter Song name-  ")
        a = input()
        b = node(a)
        b.next = self.head
        if self.head is not None:
            self.head.prev=b
        self.head=b
        self.tofile(a)

    def add_node_file(self, first, a):
        while first.next is not None:
            first = first.next
        first.next = node()
        first.prev = first
        first = first.next
        first.song = a
        first.next = None


    def del_node(self):
        temp = self.head
        if (temp != None):
            if(temp.next == None):
                temp = None
            else:
                while(temp.next.next != None):
                    temp = temp.next 
                lastNode = temp.next
                lastNode = None

    def printlist(self, playlist):
        playlistN = playlist
        print("\nPlaylist Name- {0}".format(playlistN))
        temp = self.head
        while temp is not None:
            print(temp.song)
            print("\n", end = '')
            last = temp.song
            temp = temp.next

    def printlist1(self):
        temp = self.head
        while temp is not None:
            print(temp.song)
            print("\n", end = '')
            last = temp.song
            temp = temp.next            

    def count_nodes(self):
        i = 0
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            i += 1
        i += 1
        print("\nTotal songs-  {0}".format(i))
        print("\n", end = '')

    def del_pos(self,pos):

        temp = self.head
        node_deleted = False
        count = 0

        if temp is None:
            node_deleted = False
        elif temp.song == pos:
            self.head = temp.next
            self.head.prev = None
            node_deleted = True
        else:
            temp = self.head
            while temp:
                if temp.song == pos:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    node_deleted = True
                temp = temp.next

        if node_deleted:
            count -= 1    


    def search1(self):
        print("\n\a\a\a\aEnter song To be Searched- ")
        song = input()
        flag = 0
        temp = self.head 
        a = False
        while temp is not None:
            if(temp.song == song):
                print("\n\a\a\a\a#Song Found", end = '')
                print("\n", end = '')
                a = True
                break
            temp = temp.next
            flag = flag + 1
        if a == False:
            print("\n\a\a\a\a#Song Not found", end = '')
            print("\n", end = '')

    def create(self):
        top = None

    def push(self, data):
        songs = (data)
        if self.top is None:
            self.top = node(songs)        
        else:
            a = node(songs)
            a.next = self.top
            self.top = a

    def display(self):
        top1 = self.top
        if top1 is None:
            print("\n\a\a\a\a=>NO recently played tracks.\n")
        else:
            temp = self.top
            print("\n\a\a\a\a#Recently played tracks-\n")
            while temp is not None:
                print("{0}".format(temp.song))
                print("\n", end = '')
                temp = temp.next

    def play(self):
        self.printlist1()
        print("\n\a\a\a\aChoose song you wish to play- ")
        songs = input() 
        flag = 0
        temp = self.head

        while temp is not None:
            if(temp.song == songs):
                print("\n\a\a\a\a=>Now Playing......{0}".format(songs))
                flag += 1
                self.push(songs)
                break
            else:
                temp = temp.next
        if flag == 0:
            print("\n\a\a\a\a#Song Not found")


    def recent(self):
        self.display()


    def topelement(self):
        top1 = self.top
        if top1 is None:
            print("\n\a\a\a\a#NO last played tracks.\n", end = '')
        else:    
            print("\n=>Last Played Song - ", end = '')
            print(top1.song)
            print("\n", end = '')

    def sort(self):
        
        if(self.head == None):
            print("Playlist is empty")
        else:
            current = self.head
            while(current.next != None):
                index = current.next
                while(index != None):
                    if(current.song > index.song):
                        temp = current.song
                        current.song = index.song
                        index.song = temp
                    index = index.next
                current = current.next

    def deletemenu(self):
        pos = None
        print("\nEnter the name of the song : ")
        pos = input()
        self.del_pos(pos)



choice = None
music = LinkedList()
print("\t\t\t\a\a\a\aMusic Player")
print("\n", end = '')
print("\n\n\a\a\a\aEnter the playlist name -  ")
song = input()
music.create()
condition = True

while condition:
    print("\n1.Add  New Song\n2.Delete Song\n3.Display Entered Playlist\n4.Total Songs\n5.Search Song\n6.Play Song\n7.Recently Played List\n8.Last Played\n9. Sorted playlist\n10.Exit", end = '')
    print("\n", end = '')
    print(("\n\a\a\a\aEnter your choice- "))
    choice = input()
    if choice == "1":
        music.add_node()
    if choice == "2":
        music.deletemenu()
    if choice == "3":
        music.printlist1()
    if choice == "4":
        music.count_nodes()
    if choice == "5":
        music.search1()
    if choice == "6":
        music.play()
    if choice == "7":
        music.recent()
    if choice == "8":
        music.topelement()
    if choice == "9":
        music.sort()
        music.printlist1()
    if choice == "10":
        quit()
 




