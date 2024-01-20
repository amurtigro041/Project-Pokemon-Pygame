from Project_PokemonPotions import Battle_items
from Project_PokemonPotions import Potions

class Pokemon:
    def __init__(self,name,level,Health,Atk,Defense):
        self.__name = name
        self.__HealthStandard = Health
        self.__AtkStandard =  Atk
        self.__DefStandard = Defense
        self.__Exp = 0
        self.__level = level

        #atribut masing-masing pokemon
        self.__HealthMax = self.__HealthStandard * self.__level
        self.__Atk =  self.__AtkStandard * self.__level
        self.__Defense = self.__DefStandard * self.__level

        self.__HealthStandard = self.__HealthMax
        
                  
        #self.info = "name : {}  \n\thealth : {} \n\tPower :{}".format(self.__name,self.__Health,self.__Power)
    
    @property
    def info(self):
        return "{} level {} \n\tHealth =  {}/{} \n\tAtk = {} \n\tDefense = {}".format(self.__name,self.__level,self.__HealthStandard,self.__HealthMax,self.__Atk,self.__Defense)
    
    @property
    def Gain_Exp(self):
        pass

    @property
    def Attack(self):
        pass

    @property
    def Gain_Exp (self):
        pass

    @Gain_Exp.getter
    def Gain_Exp (self):
        print('getter method called')
        return self.__Exp
    
    @Gain_Exp.setter
    def Gain_Exp (self,addExp):
        addExp = Pokemon.__level / self.__level * 100
        self.__Exp = self.__Exp + addExp

        
    def Attack(self,Pokemon):
        Pokemon.__HealthStandard = Pokemon.__HealthStandard - self.__Atk/Pokemon.__Defense
        print("{} health decreased {}".format(Pokemon.__name, Pokemon.__HealthStandard))
        if Pokemon.__HealthStandard <= 0:
            addExp = Pokemon.__level / self.__level * 100
            print("Enemy {} has fainted".format(Pokemon.__name))
            Gain_Exp = addExp
            print("{} get {} XP".format(self.__name,Gain_Exp))

        elif self.__HealthStandard <= 0:
            print("{} has fainted".format(self.__name))        

class Poke_normal(Pokemon):
    def __init__(self,name):
        super().__init__(name,1,150,200,30)
    
class Poke_Grass(Pokemon):
    pass    
class Poke_Water(Pokemon):
    pass
class Poke_Fire(Pokemon):
    pass 

Groudon= Pokemon ("Groudon",1,765,675,725)
Arceus = Poke_normal("Arceus")
Torterra = Poke_Grass("Torterra",2,575,475,4)
Polytoad =  Pokemon("Polytoad",35,600,350,477)
Gengar =  Pokemon ("Gengar",3,200,210,300)




print(Arceus._Pokemon__HealthStandard)

#Testing
Groudon.Attack(Arceus)
Arceus.Attack(Torterra)
Torterra.Attack(Gengar)
Polytoad.Attack(Gengar)
Gengar.Attack(Groudon)
Groudon.Attack(Gengar)
Arceus.Attack(Polytoad)
Gengar.Attack(Arceus)
Arceus.Attack(Groudon)
Groudon.Attack(Torterra)
Torterra.Attack(Polytoad)
Groudon.Attack(Gengar)

while Torterra._Pokemon__HealthStandard >= 500:
    Groudon.Attack(Torterra)
    print("Groudon used Normal Beam!")
    if Torterra._Pokemon__HealthStandard <= 500:
        print(f"Torterra Health is now : {Torterra._Pokemon__HealthStandard}")
        print("Groudon fled from the battle")
