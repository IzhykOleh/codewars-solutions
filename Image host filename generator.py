import random
import string

def generateName():
    name = "".join([random.choice(string.ascii_uppercase) for i in range(6)])
    return name if not photoManager.nameExists(name) else generateName()

