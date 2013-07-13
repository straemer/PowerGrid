import threading
from copy import copy

class Player:
    
    # max_resources=max capacity for each type of resource
    # [coal, oil, garbage, uranium]
    # cities = array of nodes
    # cities_powered = cites powered this turn
    def __init__(self, ):
        self.money=0
        self.resources=[0, 0, 0, 0]      
        self.cities=[]
        self.power_plants=[]
        self.max_plants=3
        self.max_resources=[0, 0, 0, 0]         
        self.cities_powered=0
        self.lock = threading.Lock()
        self.playerID = 0
    
    #returns player ID, int 
    def get_playerID(self):
        with self.lock:
            return copy(self.playerID)

    #returns int
    def get_Coal(self):
        with self.lock:
            return copy(self.resources[0])
    
    #returns int
    def get_Oil (self):
        with self.lock:
            return copy(self.resources[1])
    
    #returns int
    def get_Garbage(self):
        with self.lock:
            return copy(self.resources[2])
    
    #returns int
    def get_Uranium(self):
        with self.lock:
            return copy(self.resources[3])
    
    #returns current player's money, int
    def f_b_get_money(self):
        with self.lock:
            return copy(self.money)
    
    #returns the resources the player has, array of ints
    def getResources(self):
        with self.lock:
            return copy(self.resources)
    
    #returns the cities the player owns, array of nodes
    def get_cities(self):
        with self.lock:
            return copy(self.cities)
    
    #returns the power plants the player currently owns, array of PowerPlants
    def get_PowerPlants(self):
        with self.lock:
            return copy(self.power_plants)
    
    #returns the max number of resources the player can carry for each type, array of ints
    def get_max_resources(self):
        with self.lock:
            return copy(self.get_max_resources)
    
    #returns the number of power plants the player has powered this turn
    def get_cities_powered(self):
        with self.lock:
            return copy(cities_powered)
    
    #returns the maximum valued power plant the player currently owns
    def get_MaxValPowerPlant(self):
        with self.lock:
            sorted_plants=self.power_plants.sort(key=PowerPlant.cost)
            if sorted_plants.count==0:
                return -1
            return copy(sorted_plants[0])
    
    #set player ID
    def set_PlayerID(self, playerID):
        with self.lock:
            self.playerID=playerID
    
    #removes the power plant at index i
    def remove_PowerPlant(self, i):
        with self.lock:
            self.power_plants.remove(i)
    
    #adds a city to current player    
    def add_cities(self, city):
        with self.lock:
            self.cities.append(city)
    
    #gives the current player the amount specified
    def addMoney( self, dollars ):
        with self.lock:
            self.money += dollars
    
    #calculate the number of cities powered based on the array of plants passed in
    def calc_cities_powered(self, plants):
        with self.lock:
            tot_powered=0
            for p in plants:
                tot_powered+=p.cities_powered
            self.cities_powered=tot_powered
    
    #add a power plant to the current player
    def add_plant(self, plant):
        with self.lock:
            self.power_plants.append(plant)
        
    #sets current player's player ID, playerID:int 
    def set_playerID(self, playerID):
        with self.lock:
            self.playerID=playerID    
    
    #int num is number of coal to add to the player
    def add_Coal(self, num):
        with self.lock:
            self.resources[0]+=num

    #int num is number of oil to add to the player    
    def add_Oil(self, num): 
        with self.lock:
            self.resources[1]+=num    
    
    #int num is number of garbage to add to the player
    def add_Garbage(self, num):
        with self.lock:
            self.resources[2]+=num    
    
    #int num is number of uranium to add to the player    
    def add_Uranium(self, num):
        with self.lock:
            self.resources[3]+=num        

    #int num is number of coal to deplete
    def use_Coal(self, num):
        with self.lock:
            self.resources[0]-=num
    
    #int num is number of oil to deplete 
    def use_Oil(self, num): 
        with self.lock:
            self.resources[1]-=num    
    
    #int num is number of garbage to deplete
    def use_Garbage(self, num):
        with self.lock:
            self.resources[2]-=num    
    
    #int num is number of uranium to deplete    
    def use_Uranium(self, num):
        with self.lock:
            self.resources[3]-=num   

    #int num how much money to deplete       
    def use_money(self, num):
        with self.lock:
            self.money -= num
            
    #buys resources and subract current player's money based on the resources of each type required represented by an array  
    def buy_resources(self, resources):
        with self.lock:
            tot_cost+=buy_resources(resource[0], resource[1], resource[2], resource[3])
            if tot_cost==-1:
                return
            if tot_cost-self.money<0:
                return
            else:
                for i in range(res_resources):
                    self.resources[i]+=resources[i]
                self.money = self.money-tot_cost
    
    #buys cities based on the array of cities requested and subtracts current player's money
    def buy_cities(self, cities_req):
        with self.lock:
            tot_cost=0
            if tot_cost == -1:
                return
            if tot_cost-self.money < 0:
                return
            else:
                for r in res_req:
                    self.cities.append(r)          
