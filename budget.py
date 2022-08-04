class Category:
  

  def __init__(self, name):
    self.name = name
    self.total = 0
    self.ledger = []

    
  def deposit(self, amount, description=False):
    if not description:
      description = ""
    if description == "initial deposit":
      self.total = amount
    else:
      self.total += amount
    self.ledger.append({"amount":amount, "description": description})

  def withdraw(self, amount, description=False):
    if Category.check_funds(self, amount):
      if not description:
        description = ""
      self.ledger.append({"amount":amount*-1, "description": description})
      self.total -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.total

  def transfer(self, amount, bud_cat):
    if Category.check_funds(self,amount):
      self.withdraw(amount, f"Transfer to {bud_cat.name}")
      bud_cat.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False
    

  def check_funds(self, amount):
    if self.total - amount >= 0:
      return True
    else:
      return False


  def __repr__(self):
    Object_moves = f"{self.name:*^30}\n"
    for item in self.ledger:
      if len(item["description"]) > 23:
        Object_moves+= f'{item["description"][:23]}'+ f' {item["amount"]:>{30-len(item["description"])}.2f}\n'
      else:
        Object_moves+= f'{item["description"][:23]}'+ f'{item["amount"]:>{30-len(item["description"])}.2f}\n'
    Object_moves+= f"Total: {self.total}"
    return Object_moves

def create_spend_chart(categories):
  Percen_string = "Percentage spent by category\n"
  pers = []
  sumcats = []
  cates = []
  for category in categories:
    cates.append(category.name)

  Total_sum = 0
  for cat in categories:
    Object_sum = 0
    for item in cat.ledger:      
      if item["amount"] < 0:
        Item_amount = item["amount"]*-1
        Object_sum += Item_amount 
        Total_sum += Item_amount
    sumcats.append(Object_sum)
  for sum in sumcats:
    por = round((sum*100)/Total_sum)
    pers.append(por)
        
  
  for per in range(100,-10, -10):
    Percen_string += f"{per:>{3}}|" 
    for val in pers:
      if val >= per:
        Percen_string += "o".center(3, " ")
      else:
        Percen_string+= " "*3
    Percen_string += " \n"

  Percen_string += " "*4 + "-"*((len(categories)*3)+1) + "\n"

  # We make every Category name the same length to avoid range errors
  maxcatlen = 0
  for cat in cates:
    if len(cat) > maxcatlen:
      maxcatlen = len(cat)
  for cat in range(len(cates)):
    if len(cates[cat]) < maxcatlen: 
      cates[cat] += " "*(maxcatlen-len(cates[cat]))
    
  for lett in range(maxcatlen):
    Percen_string += " "* 5
    for cat in range(len(cates)):      
      Percen_string +=  cates[cat][lett] 
      Percen_string += "  "
    if lett + 1 != maxcatlen:
      Percen_string+= "\n"

  
  return Percen_string