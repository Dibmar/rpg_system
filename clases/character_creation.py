import random

class PC:

    species_dict = {1: 'Human', 2: 'Orc', 3: 'Dwarf', 4: 'Elf', 5: 'Cton'}
    species = ''

    def __init__ (self, name):
        self.name = name
        self.species = '____________'
        self.phisical = 0
        self.agility = 0
        self.mind = 0
        self.magic = 0
        self.strenght =  0
        self.resilience = 0
        self.celerity = 0
        self.dexterity = 0
        self.deduction = 0
        self.charisma = 0
        self.wisdom = 0
        self.choice = ''

    def general_character_sheet(self):
        print("General info on your character")
        print(f'Name: {self.name} |\tSpecies: {self.species}|')

        print("\nPC's Attributes\n-------------------------")
        print(f'PHIS: {self.phisical} |\tAGIL: {self.agility} |\nMIND: {self.mind} |\tMAG: {self.magic}  |\n-------------------------')
    
    def set_attributes(self):
        points = 8
        number = 3

        print('Time to set your attributes...')
        # print(f'You have {points} points remaining.')

        
        print('Your attributes will be chosen randomly')
        attribute_values = {(num + 1): random.randint(2, 4) for num in range(number)}
        
        if sum(attribute_values) > 8:
            operation = sum(attribute_values) - points
            print('OMG', operation, 'of excess')

            while operation != 0:
                position = random.randint(1, len(attribute_values))
                attribute_values[position] -= 1

                operation = sum(attribute_values) - points
        
        elif sum(attribute_values) < 8:
            operation = points - sum(attribute_values)
            print('omg', operation, 'of lacking')

            for i in range(operation):
                position = random.randint(1, len(attribute_values))

                if attribute_values[position] < 5:
                    if position == len(attribute_values):
                        position -= 1
                    
                    else:
                        position += 1

                    attribute_values[position] += 1
                
                else:
                    attribute_values[position] += 1

        self.phisical = attribute_values[1]
        self.agility = attribute_values[2]
        self.mind = attribute_values[3]

    def set_characteristics(self):
        number = 7
        points = 15

        self.strenght = self.phisical
        self.resilience = self.phisical

        self.celerity = self.agility
        self.dexterity = self.agility

        self.charisma = self.mind
        self.wisdom = self.mind
        self.deduction = self.mind

        characteristics_values = [num, random.randint(1, 5) for num in range(number)]
        characteristics_list = [self.strenght, self.resilience, self.celerity, self.dexterity, self.charisma, self.wisdom, self.deduction]

        print(characteristics_values)
        
        operation = points - sum(characteristics_values)
        print(operation)
        print('---------------------')

        if operation < 0:
            while operation != 0:
                
                position = random.randint(0, len(characteristics_values))
                print(position)
                operation = points - sum(characteristics_values)

                # if characteristics_values[position] > 6:

                #     if position == len(characteristics_values):
                #         position -= 1
                    
                #     else:
                #         position += 1

                characteristics_values[position] += 1

        
        elif operation > 0:
        
            position = random.randint(0, len(characteristics_values))
            print(position)
            operation = sum(characteristics_values) - points

            # print(characteristics_values)

            # if characteristics_values[position] > 6:

            #     if position == len(characteristics_values):
            #         position -= 1
                
            #     else:
            #         position += 1

            characteristics_values[position] -= 1
    
        print(characteristics_values)


    def select_species(self):

        print('Select your species:')

        for e in self.species_dict:
            print(f'\t{e}.- for {self.species_dict[e]}')

        self.choice = self.species_dict[int(input("Type your choice here (remember to use numbers!)> "))]
        self.species = self.choice

        print(f'Your character is a {self.species.lower()}')
        
        if self.species == 'Human':
            self.magic = 0
        
        else:
            self.magic = 10
    
    



char = PC(name= 'Gor')
# char.select_species()
print('------------------------------------------------------------')
char.set_attributes()
print('------------------------------------------------------------')
char.set_characteristics()
print('------------------------------------------------------------')
char.general_character_sheet()