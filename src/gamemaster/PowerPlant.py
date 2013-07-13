class PowerPlant(object):
    def __init__(self, cost, resourceTypes, resourcesRequired, housesPowered):
        self.cost = cost
        self.resourceTypes = resourceTypes
        self.resourcesRequired = resourcesRequired
        self.housesPowered = housesPowered
        
        if (resourceTypes is None):
            self.type = "STAGE3"
            self.hybrid = False
        else:
            self.type = "PowerPlant"
            if (len(resourceTypes) == 1):
                self.hybrid = False
            else:
                self.hybrid = True
    
    def __str__(self):
        return "[%r, %r, %r, %r, %r]" % (self.type, self.cost, self.resourceTypes, self.resourcesRequired, self.housesPowered)
    def __unicode__(self):
        return "[%r, %r, %r, %r, %r]" % (self.type, self.cost, self.resourceTypes, self.resourcesRequired, self.housesPowered)
    def __repr__(self):
        return "[%r, %r, %r, %r, %r]" % (self.type, self.cost, self.resourceTypes, self.resourcesRequired, self.housesPowered)
      
        
        