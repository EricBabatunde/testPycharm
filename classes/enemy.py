class Enemy:
    def __init__(self, hp, mp):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

    def getHP(self):
        return self.hp

    def getMP(self):
        return self.mp