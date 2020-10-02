from prettytable import PrettyTable
from datetime import datetime
import importlib

class Individual:
  def __init__(self, Id):
    self.Id = Id
    self.name = ""
    self.gender = ""
    self.birthDateString = ""
    self.birthDateObject = ""
    self.age = ""
    self.alive = True
    self.deathDateString = ""
    self.deathDateObject = ""
    self.childId = ""
    self.spouseFamilyIds = []
    self.errors = []
    self.anomalies = []

  def addSpouseId(self,familyId):
    self.spouseFamilyIds.append(familyId)

  def totalList(self):
    return [self.Id,self.name,self.gender,self.birthDateString,self.age,self.alive,self.deathDateString,self.childId if len(self.childId) != 0 else "",self.spouseFamilyIds if len(self.spouseFamilyIds) != 0 else "",self.errors if len(self.errors) != 0 else "",self.anomalies if len(self.anomalies) != 0 else ""]

class Family:
  def __init__(self, Id):
    self.Id = Id
    self.marriageDateString = ""
    self.marriageDateObject = ""
    self.divorceDateString = ""
    self.divorceDateObject = ""
    self.husbandId = ""
    self.husbandName = ""
    self.wifeId = ""
    self.wifeName = ""
    self.children = []
    self.errors = []
    self.anomalies = []

  def addChild(self,childId):
    self.children.append(childId)
    
  def totalList(self):
    return [self.Id,self.marriageDateString,self.divorceDateString,self.husbandId,self.husbandName,self.wifeId,self.wifeName,self.children if len(self.children) != 0 else "",self.errors if len(self.errors) != 0 else "",self.anomalies if len(self.anomalies) != 0 else ""]
    
def print_individuals_table(individual):
  Prettable = PrettyTable()
  Prettable.field_names = ["ID","Name","Gender","Birth Date","Age","Alive","Death Date","Child Family","Spouse Families","Errors","Anomalies"]
  for i in individual:
    Prettable.add_row(i.totalList())
  print("Individual")
  print(Prettable)
  
def print_families_table(family):
  Prettable = PrettyTable()
  Prettable.field_names = ["ID","Marriage Date","Divorce Date","Husband ID","Husband Name","Wife ID","Wife Name","Child IDs","Errors","Anomalies"]
  for f in family:
    Prettable.add_row(f.totalList())
  print("Family")
  print(Prettable)


labels = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

Gedcom_File = open("Zaccaria.ged", "r") 

individual = []
family = []

def populate_gedcom_data(Gedcom_File): 
  findinglabels = False
  Indiv = False
  lookingDivorce = False
  lookingDeath = False
  lookingMarriage = False
  lookingBirth = False
  currI = 0
  for k,line in enumerate(Gedcom_File):
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
            individual[len(individual)-1].addSpouseId(linelist[2].strip("@"))
          if label == "BIRT":
            lookingBirth = True
          if label == "DEAT":
            lookingDeath = True
          if lookingBirth:
            birthDate_string = " ".join(linelist[2:])
            birthDate_object = datetime.strptime(birthDate_string, '%d %b %Y')
            individual[len(individual)-1].birthDateString = birthDate_string
            individual[len(individual)-1].birthDateObject = birthDate_object
            individual[len(individual)-1].age = str((datetime.now() - birthDate_object)/365).split(" ")[0]
            lookingBirth = False
          if lookingDeath:
            individual[len(individual)-1].deathDateString = " ".join(linelist[2:])
            deathDate_object = datetime.strptime(individual[len(individual)-1].deathDateString, '%d %b %Y')
            individual[len(individual)-1].age = str((deathDate_object - individual[len(individual)-1].birthDateObject)/365).split(" ")[0]
            individual[len(individual)-1].alive = False
            lookingDeath = False
        except:
          pass
      else:
        try:
          if lookingMarriage:
            family[len(family)-1].marriageDateString = " ".join(linelist[2:])
            family[len(family)-1].marriageDateObject = datetime.strptime(family[len(family)-1].marriageDateString, '%d %b %Y')
            lookingMarriage = False
          if label == "HUSB":
            hid = linelist[2].strip("@")
            family[len(family)-1].husbandId = hid
            for ind in individual:
              if ind.Id == hid:
                family[len(family)-1].husbandName = ind.name
          if label == "WIFE":
            wid = linelist[2].strip("@")
            family[len(family)-1].wifeId = wid
            for ind in individual:
              if ind.Id == wid:       
                family[len(family)-1].wifeName = ind.name 
          if label == "MARR":
            lookingMarriage = True
          if lookingDivorce:
            family[len(family)-1].divorceDateString = " ".join(linelist[2:])
            family[len(family)-1].divorceDateObject = datetime.strptime(family[len(family)-1].divorceDateString, '%d %b %Y')
            lookingDivorce = False
          if label == "DIV":
            lookingDivorce = True  
          if label == "CHIL":
            family[len(family)-1].addChild(linelist[2].strip("@"))
            
        except:
          pass


populate_gedcom_data(Gedcom_File)
print_individuals_table(individual)
print('\n')
print_families_table(family)