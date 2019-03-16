class Router(object):

    def __init__(self):
        self.f = 0
        self.url = ""
        self.method = ""
        
    def bind(self, url, method, f):
        self.url = url[:]
        self.method = method[:]
        self.f = f
        
    def runRequest(self, url, method):
        if self.method == method:
            if self.url == url:
                return self.f()
        else:
            return "Error 404: Not Found"
