class Player:
    money=0
    resources=[]
    cities=[]
    power_plants=[]
    max_plants=3
    max_resources=[]
    
    

    def bid():
        valid=false
        while valid==false:
            plant = int(input('Enter plant no.'))
            cur_bid=int(input('Enter bid'))
            if cur_bid==-1:
                return
            result=get_bid(plant,cur_bid)
            if result==true:
                valid=true
            
    def update_bid(outbid, plant, maxbid):
        if outbid:
            valid=false
            while valid==false:
                cur_bid=int(input('Enter bid'))
                if cur_bid==-1:
                    return
                result=get_bid(plant,cur_bid)          
                if result==true:
                    valid=true            
        else:
            if power_plants.count>3
            remove_powerPlant()
            power_plants.append(getPlant(plant))
            money=money-maxbid
            
    def remove_powerPlant():
        valid=false
        while valid==false:
            plant_no=int(input('Enter power plant to remove (1-3)'))
            if plant_no>0 and plant_no<4:
                power_plants.remove(plant_no)
            
    def get_resources(res_req):
        tot_cost=0
        if tot_cost==-1:
            return
        if tot_cost-money<0:
            return
        else:
            for r in res_req:
                resources.append(r)
            money = money-tot_cost
    
    def buy_cities(cities_req):
        tot_cost=0
        if tot_cost == -1:
            return
        if tot_cost-money < 0:
            return
        else:
            for r in res_req:
                cities.append(r)        


class PowerPlant:
    cost=0
    cities_powered=0
    resource_types=[]
    resource_capacity=0
    resources_req=0

