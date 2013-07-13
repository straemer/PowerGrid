import src.gamemaster.PowerPlant
import src.gamemaster.Resource

class Player:
    
    def __init__(self):
        self.money=0
        #[coal, oil, garbage, uranium]
        self.resources=[0, 0, 0, 0]
        self.cities=[]
        self.power_plants=[]
        self.max_plants=3
        
        #max capacity
        self.max_resources=[0, 0, 0, 0]  
        
        self.cities_powered=0

    def get_Coal(self):
        return self.resources[0]
    
    def get_Oil (self):
        return self.resources[1]
    
    def get_Garbage(self):
        return self.resources[2]
    
    def get_Uranium(self):
        return self.resources[3]
    
    def add_Coal(self, num):
        self.resources[0]+=num
        
    def add_Oil(self, num): 
        self.resources[1]+=num    
    
    def add_Garbage(self, num):
        self.resources[2]+=num    
        
    def add_Uranium(self, num):
        self.resources[3]+=num        

    def use_Coal(self, num):
        self.resources[0]-=num
        
    def use_Oil(self, num): 
        self.resources[1]-=num    
    
    def use_Garbage(self, num):
        self.resources[2]-=num    
        
    def use_Uranium(self, num):
        self.resources[3]-=num   

    def use_money(self, num):
        self.money -= num
    
    def f_b_get_money(self):
        return self.money
    
    def getResources(self):
        return self.resources
    
    def get_cities(self):
        return self.cities
    
    def get_PowerPlants(self):
        return self.power_plants
    
    def get_max_resources(self):
        return self.get_max_resources
    
    def remove_PowerPlant(self, i):
        self.power_plants.remove(i)
    
    def remove_resources(self, i):
        self.resources.remove(i)
        
    def add_cities(self, city):
        self.cities.append(city)
    
    def addMoney( self, dollars ):
        self.money += dollars
    
    def calc_cities_powered(self, plants):
        tot_powered=0
        for p in plants:
            tot_powered+=p.cities_powered
        self.cities_powered=tot_powered
    
    def add_plant(self, plant):
        self.power_plants.append(plant)
    
    def get_cities_powered(self):
        return cities_powered
    
    def get_MaxValPowerPlant(self):
        sorted_plants=self.power_plants.sort(key=PowerPlant.cost)
        if sorted_plants.count==0:
            return -1
        return sorted_plants[0]
    
    def add_resources(self, resources):
        for r in resources:
            self.resources.append(r)
    
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
    
    def buy_cities(cities_req):
        tot_cost=0
        if tot_cost == -1:
            return
        if tot_cost-self.money < 0:
            return
        else:
            for r in res_req:
                self.cities.append(r)          
'''      
    def bid():
        valid=False
        while valid==False:
            plant = int(input('Enter plant no.'))
            cur_bid=int(input('Enter bid'))
            if cur_bid==-1:
                return
            result=get_bid(plant, )
            if result==true:
                valid=true
            
    def update_bid(self, outbid, plant, maxbid):
        if outbid:
            valid=False
            while valid==False:
                cur_bid=int(input('Enter bid'))
                if cur_bid==-1:
                    return
                result=get_bid(plant,cur_bid)          
                if result==true:
                    valid=true            
        else:
            if power_plants.count>3
            remove_powerPlant(self)
            self.power_plants.append(getPlant(plant))
            self.money=self.money-maxbid
            
    def remove_powerPlant(self):
        valid=False
        while valid==False:
            plant_no=int(input('Enter power plant to remove (1-3)'))
            if plant_no>0 and plant_no<4:
                self.power_plants.remove(plant_no) 
      


class PowerPlant:
    cost=0
    cities_powered=0
    resource_types=[]
    resource_capacity=0
    resources_req=0 '''
            

