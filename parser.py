from prettytable import PrettyTable
from datetime import datetime
import importlib

class Individual:
  def __init__(self, Id):
    self.Id = Id
    self.name = ""
    self.gender = ""
    self.birthDate = ""
    self.age = ""
    self.alive = True
    self.deathDate = ""
    self.childId = ""
    self.spouseId = ""
    self.errors = []
    self.anomalies = []

  def totalList(self):
    return [self.Id,self.name,self.gender,self.birthDate,self.age,self.alive,self.deathDate,self.childId if len(self.childId) != 0 else "N/A",self.spouseId,self.errors if len(self.errors) != 0 else "",self.anomalies if len(self.anomalies) != 0 else ""]

class Family:
  def __init__(self, Id):
    self.Id = Id
    self.married = ""
    self.divorced = ""
    self.husbandId = ""
    self.husbName = ""
    self.wifeId = ""
    self.wifeName = ""
    self.children = []
    self.errors = []
    self.anomalies = []

  def addChild(self,childId):
    self.children.append(childId)
    
  def totalList(self):
    return [self.Id,self.married,self.divorced,self.husbandId,self.husbName,self.wifeId,self.wifeName,self.children if len(self.children) != 0 else "N/A",self.errors if len(self.errors) != 0 else "",self.anomalies if len(self.anomalies) != 0 else ""]
    
def print_individuals_table(individual):
  Prettable = PrettyTable()
  Prettable.field_names = ["ID","Name","Gender","BirthDate","Age","Alive","DeathDate","ChildId","SpouseId","Errors","Anomalies"]
  for i in individual:
    Prettable.add_row(i.totalList())
  print("Individual")
  print(Prettable)
  
def print_families_table(family):
  Prettable = PrettyTable()
  Prettable.field_names = ["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Child ID","Errors","Anomalies"]
  for f in family:
    Prettable.add_row(f.totalList())
  print("Family")
  print(Prettable)


labels = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

Gedcomm_File = open("Zaccaria.ged", "r")

individual = []
family = []

def populate_gedcom_data(Gedcomm_File): 
  findinglabels = False
  Indiv = False
  lookingDivorce = False
  lookingDeath = False
  lookingMarriage = False
  lookingBirth = False
  currI = 0
  for k,line in enumerate(Gedcomm_File):
    line = line.replace("\n","")
    linelist = line.split(" ")
    k = linelist[1]
    if k[0] == "@":
      if k[1] == "F":
        family.append(Family(k[1:-1]))
        Indiv = False
      if k[1] == "I":
        individual.append(Individual(k[1:-1]))    
        Indiv = True
      findinglabels = True
    elif findinglabels:
      label = linelist[1]
      if Indiv:
        try:
          if label == "NAME":
            individual[len(individual)-1].name = " ".join(linelist[2:])
          if label == "SEX":
            individual[len(individual)-1].gender = linelist[2]
          if label == "FAMC":
            individual[len(individual)-1].childId = linelist[2].strip("@")
          if label == "FAMS":
            individual[len(individual)-1].spouseId = linelist[2].strip("@")
          if label == "BIRT":
            lookingBirth = True
          if label == "DEAT":
            lookingDeath = True
          if lookingBirth:
            birthDate = " ".join(linelist[2:])
            birthDate_object = datetime.strptime(birthDate, '%d %b %Y')
            individual[len(individual)-1].birthDate = birthDate
            individual[len(individual)-1].age = str((datetime.now() - birthDate_object)/365).split(" ")[0]
            lookingBirth = False
          if lookingDeath:
            individual[len(individual)-1].deathDate = " ".join(linelist[2:])
            birth_object = datetime.strptime(individual[len(individual)-1].birthDate, '%d %b %Y')
            death_object = datetime.strptime(individual[len(individual)-1].deathDate, '%d %b %Y')
            individual[len(individual)-1].age = str((death_object - birth_object)/365).split(" ")[0]
            individual[len(individual)-1].alive = False
            lookingDeath = False  
        except:
          pass
      else:
        try:
          if lookingMarriage:
            family[len(family)-1].married = " ".join(linelist[2:])
            lookingMarriage = False
          if label == "HUSB":
            hid = linelist[2].strip("@")
            family[len(family)-1].husbandId = hid
            for ind in individual:
              if ind.Id == hid:
                family[len(family)-1].husbName = ind.name
          if label == "WIFE":
            wid = linelist[2].strip("@")
            family[len(family)-1].wifeId = wid
            for ind in individual:
              if ind.Id == wid:       
                family[len(family)-1].wifeName = ind.name 
          if label == "MARR":
            lookingMarriage = True
          if lookingDivorce:
            family[len(family)-1].divorced = " ".join(linelist[2:])
            lookingDivorce = False
          if label == "DIV":
            lookingDivorce = True  
          if label == "CHIL":
            family[len(family)-1].addChild(linelist[2].strip("@"))
            
        except:
          pass
      

populate_gedcom_data(Gedcomm_File)
print_individuals_table(individual)
print('\n')
print_families_table(family)