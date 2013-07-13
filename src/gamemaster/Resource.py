

class Resource:
  # Initialize resource on board
  coal = 24
  oil = 18
  garbage = 6
  uranium = 2

  GENERAL_MAX = 24
  URANIUM_MAX = 12

  numPlayer = 2
  phase = 1   # always start at phase 1
  resources = [0, 0, 0, 0]    # resource in order of c, o, g, u

  # Market Price
  # index corresponds to price -1 of the slot on gameboard
  # value in the slot is the number of resources available at that price
  coalPrice = [3, 3, 3, 3, 3, 3, 3, 3]
  oilPrice = [0, 0, 3, 3, 3, 3, 3, 3]
  garbagePrice = [0, 0, 0, 0, 0, 0, 3, 3]
  uraniumPrice = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
  coalIndex = 0
  oilIndex = 2
  garbageIndex = 6
  uraniumIndex = 10

  # Init method to initialize how many players are in the game, and the phase of the game
  def __init__(self, numOfPlayer):
    self.numPlayer = numOfPlayer
    self.__update_resource_restore_amount()

  # Update game phase, since it is possible to jump from phase 1 to 3
  def update_game_phase(self, gamePhase):
    self.phase = gamePhase
    self.__update_resource_restore_amount()

  # Buy resources
  # params: coal, oil, garbage, uranium
  # returns: cost, 0 if not suffient resource
  def buy_resources(self, c, o, g, u):
    if (c > self.coal or o > self.oil or g > self.garbage or u > self.uranium):
      return 0
    totalCost = 0
    if (c > 0):
      returnedTuple = self.__calculatePrice(c, self.coalPrice, self.coalIndex)
      self.coalPrice = returnedTuple[0]
      self.coalIndex = returnedTuple[1]
      totalCost += returnedTuple[2]
      self.coal -= c
    if (o > 0):
      returnedTuple = self.__calculatePrice(o, self.oilPrice, self.oilIndex)
      self.oilPrice = returnedTuple[0]
      self.oilIndex = returnedTuple[1]
      totalCost += returnedTuple[2]
      self.oil -= o
    if (g > 0):
      returnedTuple = self.__calculatePrice(g, self.garbagePrice, self.garbageIndex)
      self.garbagePrice = returnedTuple[0]
      self.garbageIndex = returnedTuple[1]
      totalCost += returnedTuple[2]
      self.garbage -= g
    if (u > 0):
      self.uranium -= u
      left = u
      while (left > 0):
        self.uraniumPrice[self.uraniumIndex] = 0
        if (self.uraniumIndex == 8):
          totalCost += 10
        elif (self.uraniumIndex == 9):
          totalCost += 12
        elif (self.uraniumIndex == 10):
          totalCost += 14
        elif (self.uraniumIndex == 11):
          totalCost += 16
        else:
          totalCost = totalCost + self.uraniumIndex + 1
        self.uraniumIndex += 1
        left -= 1
    return totalCost

  # BEGIN debug methods
  def print_all_resource_stock_list(self):
    self.__print_stock_list(self.coalPrice)
    self.__print_stock_list(self.oilPrice)
    self.__print_stock_list(self.garbagePrice)
    self.__print_stock_list(self.uraniumPrice)

  def __print_stock_list(self, array):
    string = ''
    for x in array:
      string += str(x) + " "
    print (string)

  def print_resource_restock_amount(self):
    string = ''
    for x in self.resources:
      string += str(x) + " "
    print (string)
  # END debug methods
                
  # helper method to calculate cost
  def __calculatePrice(self, r, price, priceIndex):
    cost = 0
    while (r > 0):
      if (r >= 3):
        r -= 3
        if (priceIndex < 7):
          price[priceIndex+1] = price[priceIndex]
        cost = cost + price[priceIndex]*(priceIndex+1) + (3-price[priceIndex])*(priceIndex+2)
        price[priceIndex] = 0
        priceIndex += 1
      else:
        if (price[priceIndex] < r):
          price[priceIndex+1] = 3 - r + price[priceIndex]
          cost += price[priceIndex]*(priceIndex+1)
          price[priceIndex] = 0
        else:
          price[priceIndex] -= r
          cost += r*(priceIndex+1)

        if (priceIndex < 7 and price[priceIndex+1] != 3):
          cost += (3 - price[priceIndex+1])*(priceIndex+2)
        if (price[priceIndex] == 0):
          priceIndex += 1
        r = 0
    return (price, priceIndex, cost)

  # show resources
  def show_resources(self):
    print ("Coal: " + str(self.coal) + ", Oil: " + str(self.oil) + ", Garbage: " + str(self.garbage) + ", Uranium: " + str(self.uranium))

  # Restore resources
  def restore_resources(self):
    if (self.coal + self.resources[0] > self.GENERAL_MAX):
      self.coal = self.GENERAL_MAX
    else:
      self.coal += self.resources[0]
    if (self.oil + self.resources[1] > self.GENERAL_MAX):
      self.oil = self.GENERAL_MAX
    else:
      self.oil += self.resources[1]
    if (self.garbage + self.resources[2] > self.GENERAL_MAX):
      self.garbage = self.GENERAL_MAX
    else:
      self.garbage += self.resources[2]
    if (self.uranium + self.resources[3] > self.URANIUM_MAX):
      self.uranium = self.URANIUM_MAX
    else:
      self.uranium += self.resources[3]

    returnedTuple = self.__restore_general(self.resources[0], self.coalPrice, self.coalIndex)
    self.coalPrice = returnedTuple[0]
    self.coalIndex = returnedTuple[1]
 
    returnedTuple = self.__restore_general(self.resources[1], self.oilPrice, self.oilIndex)
    self.oilPrice = returnedTuple[0]
    self.oilIndex = returnedTuple[1]

    returnedTuple = self.__restore_general(self.resources[2], self.garbagePrice, self.garbageIndex)
    self.garbagePrice = returnedTuple[0]
    self.garbageIndex = returnedTuple[1]

    left = self.resources[3]
    while (left > 0):
      if (self.uraniumPrice[self.uraniumIndex] == 1):
        self.uraniumIndex -= 1
      left -= 1      
      self.uraniumPrice[self.uraniumIndex] = 1
    if (self.uraniumPrice[self.uraniumIndex] == 0):
      self.uraniumIndex += 1


  # helper method for restore resources
  def __restore_general(self, num, price, priceIndex):
    while (num > 0 and priceIndex >= 0):
      if (price[priceIndex] == 3):
        priceIndex -= 1
      if (priceIndex < 0):
        break
      if (num > (3-price[priceIndex])):
        num -= price[priceIndex]
        price[priceIndex] = 3
      else:
        price[priceIndex] += num
        num = 0        
      
    if (price[priceIndex] == 0):
      priceIndex += 1
    return (price, priceIndex)

  # Update resource restore amount, this is part of the game rule
  def __update_resource_restore_amount(self):
    if (self.numPlayer == 2):
      if (self.phase == 1):
        self.resources = [3, 2, 1, 1]
      elif (self.phase == 2):
        self.resources = [4, 2, 2, 1]
      elif (self.phase == 3):
        self.resources = [3, 4, 3, 1]
    elif (self.numPlayer == 3):
      if (self.phase == 1):
        self.resources = [4, 2, 1, 1]
      elif (self.phase == 2):
        self.resources = [5, 3, 2, 1]
      elif (self.phase == 3):
        self.resources = [3, 4, 3, 1]
    elif (self.numPlayer == 4):
      if (self.phase == 1):
        self.resources = [5, 3, 2, 1]
      elif (self.phase == 2):
        self.resources = [6, 4, 3, 2]
      elif (self.phase == 3):
        self.resources = [4, 5, 4, 2]
    elif (self.numPlayer == 5):
      if (self.phase == 1):
        self.resources = [5, 4, 3, 2]
      elif (self.phase == 2):
        self.resources = [7, 5, 3, 3]
      elif (self.phase == 3):            
        self.resources = [5, 6, 5, 2]
    elif (self.numPlayer == 6):
      if (self.phase == 1):
        self.resources = [7, 5, 3, 2]
      elif (self.phase == 2):
        self.resources = [9, 6, 5, 3]
      elif (self.phase == 3):
        self.resources = [6, 7, 6, 3]
 


# Main
#resources = Resource(3)
#resources.print_resource_restock_amount()
#resources.print_all_resource_stock_list()
#resources.restore_resources()
#print ('')
#resources.print_all_resource_stock_list()


