import random
class Ghost():
    def __init__(self):
        self.color = ["red","purple","yellow","white"][random.randint(0,3)]
        color = self.color
ghost = Ghost()
print(ghost.color)