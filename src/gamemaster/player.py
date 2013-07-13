class Player:

	
    money=0
    resources=[]
    cities=[]
    power_plants=[]
    max_plants=3
    max_resources=[]
    cities_powered=0
    
    def __init__(self):
        self.money=0
        self.resources=[]
        self.cities=[]
        self.power_plants=[]
        self.max_plants=3
        self.max_resources=[]  
        self.cities_powered=0
    
    def f_b_get_money(self):
        return self.money
    
    def get_resources(self):
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
    
    def get_cities_powered(self):
        return cities_powered
    
    def get_MaxValPowerPlant(self):
        sorted_plants=self.power_plants.sort(key=PowerPlant.cost)
        if sorted_plants.count==0:
            return -1
        return sorted_plants[0]
    
    def buy_resources(self, res_req):
        tot_cost=0
        if tot_cost==-1:
            return
        if tot_cost-self.money<0:
            return
        else:
            for r in res_req:
                self.resources.append(r)
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
 """  placeholders         
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
    resources_req=0 """
            

