# Hugo Paulat - Assignment 4 - melody.py
#December 5, 2022

from note import *

class Melody():
    """
    A class that represents a Melody.
    
    Instance Attributes:
    *self.title = output_PGM_list[0]
    *self.author = output_PGM_list[1]
    *self.notes = []
    """
    
    def __init__(self, filename):
        """(str) --> list
        Iterates through the file in a correct format, and returns a correct list of objects.
        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25
        >>> print(happy_birthday.notes[3])
        0.5 D 4 natural
        >>> print(happy_birthday.notes[1])
        0.25 D 4 natural
        """
        output_PGM_list = []
        
        fobj = open(filename, "r")
        for line in fobj:
            output_PGM_list.append(line.strip("\n"))
        self.title = output_PGM_list[0]
        self.author = output_PGM_list[1]
        
        self.notes = []
        
        x = 2
        repeat = False
        for items in output_PGM_list[2:]:
            
            inside_items = items.split(" ")
            duration = float(inside_items[0])
            pitch = inside_items[1]
            octave = int(inside_items[2])
            accidental = inside_items[3].lower()
            self.notes.append(Note(duration, pitch, octave,accidental))
            
            if inside_items[4] == "true":
                if not repeat:
                    starting_index = x
                    repeat = True
                
                else:
                    ending_index = x
                    repeat = False  

                    for i in range(1):
                        for items in output_PGM_list[starting_index:ending_index+1]:
                            inside_items = items.split(" ")
                            duration = float(inside_items[0])
                            pitch = inside_items[1]
                            octave = int(inside_items[2])
                            accidental = inside_items[3].lower()
                        
                            self.notes.append(Note(duration, pitch, octave,accidental))
            x += 1
            
            
 
            
    def play(self, player):
        for item in (self.notes):
            Note.play(item,player)


    def get_total_duration(self):
        """()--> float
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        >>> happy_birthday = Melody("fur_elise.txt")
        25.8
        >>> happy_birthday = Melody("ds.txt")
        FileNotFoundError: [Errno 2] No such file or directory: 'ds.txt'
        """
        
        total_duration = 0
        for item in (self.notes):
            total_duration += item.duration
        return (round(total_duration,2))
        
        
    def lower_octave(self):
        """() --> list
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[4].octave
        3
        >>> hotcrossbuns = Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.lower_octave()
        True
        >>> hotcrossbuns.notes[1]
        3
        >>> hotcrossbuns.notes[2]
        3
        """
        for item in (self.notes):
            if item.octave == Note.OCTAVE_MIN:
                return False
        
        for item in (self.notes):
            item.octave -= 1
                
        return True
            
    
    def upper_octave(self):
        """() --> list
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[4].octave
        4
        >>> hotcrossbuns = Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.upper_octave()
        True
        >>> hotcrossbuns.notes[1]
        4
        >>> hotcrossbuns.notes[2]
        4
        """
        
        for item in (self.notes):
            if item.octave == Note.OCTAVE_MAX:
                return False
        for item in (self.notes):
            item.octave +=1
                
        return True
    
    def change_tempo(self, multiplier):
        """() --> list
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(0.5)
        >>> happy_birthday.get_total_duration()
        6.5
        >>> hotcrossbuns = Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.get_total_duration()
        4.0
        >>> furelise = Melody("fur_elise.txt")
        >>> furelise.get_total_duration()
        """
        
        for item in (self.notes):
            item.duration *= multiplier
            
    
    
    
    
            