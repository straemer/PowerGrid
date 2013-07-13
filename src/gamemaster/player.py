
class Player:
    
    # max_resources=max capacity for each type of resource
    # [coal, oil, garbage, uranium]
    # cities = array of nodes
    # cities_powered = cites powered this turn
    def __init__(self):
        self.money=0
        self.resources=[0, 0, 0, 0]      
        self.cities=[]
        self.power_plants=[]
        self.max_plants=3
        self.max_resources=[0, 0, 0, 0]         
        self.cities_powered=0

    #returns int
    def get_Coal(self):
        return self.resources[0]
    
    #returns int
    def get_Oil (self):
        return self.resources[1]
    
    #returns int
    def get_Garbage(self):
        return self.resources[2]
    
    #returns int
    def get_Uranium(self):
        return self.resources[3]
    
    #int num is number of coal to add to the player
    def add_Coal(self, num):
        self.resources[0]+=num
    
    #int num is number of oil to add to the player    
    def add_Oil(self, num): 
        self.resources[1]+=num    
    
    #int num is number of garbage to add to the player
    def add_Garbage(self, num):
        self.resources[2]+=num    
    
    #int num is number of uranium to add to the player    
    def add_Uranium(self, num):
        self.resources[3]+=num        

    #int num is number of coal to deplete
    def use_Coal(self, num):
        self.resources[0]-=num
    
    #int num is number of oil to deplete 
    def use_Oil(self, num): 
        self.resources[1]-=num    
    
    #int num is number of garbage to deplete
    def use_Garbage(self, num):
        self.resources[2]-=num    
    
    #int num is number of uranium to deplete    
    def use_Uranium(self, num):
        self.resources[3]-=num   

    #int num how much money to deplete       
    def use_money(self, num):
        self.money -= num
    
    #returns current player's money, int
    def f_b_get_money(self):
        return self.money
    
    #returns the resources the player has, array of ints
    def getResources(self):
        return self.resources
    
    #returns the cities the player owns, array of nodes
    def get_cities(self):
        return self.cities
    
    #returns the power plants the player currently owns, array of PowerPlants
    def get_PowerPlants(self):
        return self.power_plants
    
    #returns the max number of resources the player can carry for each type, array of ints
    def get_max_resources(self):
        return self.get_max_resources
    
    #removes the power plant at index i
    def remove_PowerPlant(self, i):
        self.power_plants.remove(i)
    
    #adds a city to current player    
    def add_cities(self, city):
        self.cities.append(city)
    
    #gives the current player the amount specified
    def addMoney( self, dollars ):
        self.money += dollars
    
    #calculate the number of cities powered based on the array of plants passed in
    def calc_cities_powered(self, plants):
        tot_powered=0
        for p in plants:
            tot_powered+=p.cities_powered
        self.cities_powered=tot_powered
    
    #add a power plant to the current player
    def add_plant(self, plant):
        self.power_plants.append(plant)
    
    #returns the number of power plants the player has powered this turn
    def get_cities_powered(self):
        return cities_powered
    
    #returns the maximum valued power plant the player currently owns
    def get_MaxValPowerPlant(self):
        sorted_plants=self.power_plants.sort(key=PowerPlant.cost)
        if sorted_plants.count==0:
            return -1
        return sorted_plants[0]
    
    #buys resources and subract current player's money based on the resources of each type required represented by an array  
    def buy_resources(self, resources):
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
        tot_cost=0
        if tot_cost == -1:
            return
        if tot_cost-self.money < 0:
            return
        else:
            for r in res_req:
                self.cities.append(r)          
