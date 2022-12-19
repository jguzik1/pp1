class song():
    def __init__(self,artist,title,album,year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return f'''
Performer: {self.artist}
Song:      {self.title}
Album:     {self.album}
Year:      {self.year}
        '''

example1 = song('Ed Sheeran','Hearts Don\'t Break Srond Here','Divide','2017')
example2 = song('aaa','bbb','ccc','1234')
example3 = song('ddd','eee','fff','1238')
print(example1,example2,example3)