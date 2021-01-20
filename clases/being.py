# Libraries
import numpy as np
import json

# Class

class Being:
    
    species_dict = {0: 'Human', 1: 'Orc', 2: 'Dwarf', 3: 'Elf', 4: 'Cton'}
    role_dict = {0: 'Crafter', 1: 'Tracker', 2: 'Thief', 3: 'Warrior', 4: 'Scholar'}

    def __init__(self, name, major_character = False):
        self.name = name
        self.species = ''
        self.major_character = major_character
        
        # Attributes
        self.phisical = 0
        self.agility = 0
        self.mind = 0
        self.magic = 0

        # Characteristics

        ## Derived from phisical 
        self.strenght =  0
        self.resilience = 0
        self.health = 0
        
        ## Derived from celerity
        self.celerity = 0
        self.dexterity = 0
        
        ## Derived from mind
        self.deduction = 0
        self.charisma = 0
        self.wisdom = 0
    
    def set_attributes(self):

        threshold = 8
        if self.major_character == False:
            attributes = [self.phisical, self.agility, self.mind]

            for pos in range(len(attributes)):
                attributes[pos] = np.random.randint(1, 4)
            
            result = sum(attributes)

            if result != threshold:
                if result < threshold:
                    while result < threshold:

                        for pos in range(len(attributes)):
                            if attributes[pos] <= 3:
                                attributes[pos] += 1
                        
                        result = sum(attributes)
                
                if result > threshold:
                    while result > threshold:

                        for pos in range(len(attributes)):
                            if (attributes[pos] - 1) > 1:
                                attributes[pos] -= 1
                        
                        result = sum(attributes)
            
            self.phisical = attributes[0]
            self.agility = attributes[1]
            self.mind = attributes[2]

        else:
            """TODO A selector for customization"""
            pass


    def set_characteristics(self):
        threshold = 15

        ## Derived from phisical 
        self.strenght =  self.phisical
        self.resilience = self.phisical
        self.health = self.resilience
        
        ## Derived from celerity
        self.celerity = self.agility
        self.dexterity = self.agility
        
        ## Derived from mind
        self.deduction = self.mind
        self.charisma = self.mind
        self.wisdom = self.mind

        if self.major_character == False:
            characteristics = [self.strenght, self.resilience, self.celerity, self.dexterity, self.deduction, self.charisma, self.wisdom]

            print(characteristics)
            for pos in range(len(characteristics)):
                number = np.random.randint(0, 5)
                characteristics[pos] = characteristics[pos] + number

            result = sum(characteristics)    
            if result != threshold:
                if result < threshold:
                    while result < threshold:

                        for pos in range(len(characteristics)):
                            if characteristics[pos] <= 4:
                                characteristics[pos] += 1
                        
                        result = sum(characteristics)

                if result > threshold:
                    while result < threshold:

                        for pos in range(len(characteristics)):
                            if characteristics[pos] > 0:
                                characteristics[pos] -= 1
                        
                        result = sum(characteristics)

            # Phisical
            self.strenght += characteristics[0]
            self.resilience += characteristics[1]
            
            # Agility
            self.celerity += characteristics[2]
            self.dexterity += characteristics[3]

            # Mind
            self.deduction += characteristics[4]
            self.charisma += characteristics[5]
            self.wisdom += characteristics[6]
        
        else:
            pass


    def set_species(self):
        pass


    def set_skills(self):
        pass


    def print_character_sheet(self):

        att_to_print = f'PHI: {self.phisical} | AGI: {self.agility} | MIND: {self.mind}'
        char_to_print = f'STR: {self.strenght}  | RES: {self.resilience}  | HEALTH: {self.health}'
        char_to_print_1 = f'CEL: {self.celerity}  | DEX: {self.dexterity}  |'
        char_to_print_2 = f'DED: {self.deduction}  | CHAR: {self.charisma} | WIS: {self.mind}'
        
        print('\tCHARACTER SHEET')
        print('\t--------------------')

        print('Attributes:')
        print(att_to_print)
        print('-'*len(char_to_print_2))

        print('Characteristics:')
        print(char_to_print)
        print(char_to_print_1)
        print(char_to_print_2)
        print('-'*len(char_to_print))


orc = Being(name= 'orc', major_character= False)
orc.set_attributes()
orc.set_characteristics()
orc.print_character_sheet()

