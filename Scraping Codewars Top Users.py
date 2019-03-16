from bs4 import BeautifulSoup
import urllib.request as request
URL = 'https://www.codewars.com/users/leaderboard'

class User:
    def __init__(self, name, clan, honor):
        self.name = name
        self.clan = '' if clan == None else clan
        self.honor = int(''.join(honor.split(',')))
        
    def __str__(self):
        return 'name: %s, clan: %s, honor: %s' % (self.name, self.clan, self.honor)
        

class Leaderboard:
    def __init__(self, users = []):
        self.users = users
    
    @property
    def position(self):
        return self
        
    def __getitem__(self, position):
        return self.users[position-1]
        
    def __len__(self):
        return len(self.users)
        
    def append(self, user):
        self.users+=[user]
        
    def __iter__(self):
	    self.current_iteration = 0
	    return self
        
    def __next__(self):
	    if self.current_iteration < len(self.users):
		    user = self.users[self.current_iteration]
		    self.current_iteration+=1
		    return user
	    else:
		    raise StopIteration

def f(tag):
    return tag.name == 'tr' and tag.has_attr('data-username')

def solution():
    ro = request.urlopen(URL)
    bytes = ro.read()
    html_doc = bytes.decode("utf8")
    soup = BeautifulSoup(html_doc, 'html.parser')
    tr_tags = soup.find_all(f)
    l = Leaderboard()
    for tr in tr_tags:
        l.append(User(tr['data-username'], tr.contents[-2].string, tr.contents[-1].string))
    return l
