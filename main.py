#!/usr/bin/env python

#import modules

#character
class Character:
    def __init__(self, title, stats, items):
        self.title = title
        self.stats = stats
        self.items = items
        

#item
class Item:
    def __init__(self, title, stats):
        self.title = title
        self.stats = stats
        
    def use(self):
        pass
    
    def info(self):
        print self.title
        for stat in self.stats:
            print stat

#monster
class Monster(Character):
    def taunt(self):
        print 'Grrrr!'

#player
class Player(Character):
    def equipment(self):
        for item in self.items:
            print item

#nonplayercharacter
class NonPlayerCharacter(Character):
    def greeting(self):
        pass

#queen
class Queen(NonPlayerCharacter):
    def greeting(self):
        print 'Hello.'



if __name__ == "__main__":
    
    print 'Welcome. What is your name?'
    
    name = raw_input('Name: ')
    player = Player(name, [10,10], ['staff','piano','light','bread'])
    
    print 'Loading game...'
    
    print 'You arrive in front of the Queen\'s thrown. The aura is serious. You bow and wait for her command.'
    
    print 'Queen: Welcome, ' + player.title + '. Please rise.'
    
    monster = Monster('Monster!', [10,10],[])
    monster.taunt()
    
    
    queen = NonPlayerCharacter("Queen",[10,10],['wand','hair','crown'])