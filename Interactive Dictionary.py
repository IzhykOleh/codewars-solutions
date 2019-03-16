class Dictionary():
    def __init__(self):
        self.data = ""
        
    def newentry(self, word, definition):
        self.data+=":".join([word, definition + ';'])
        
    def look(self, key):
        index = self.data.find(key)
        if index!=-1:
            return self.data[index + len(key) + 1 : self.data.find(';', index)]
        else:
            return "Can't find entry for %s" %key
