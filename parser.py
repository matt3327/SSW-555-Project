from prettytable import PrettyTable
from datetime import datetime
import importlib
import sys

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
  print("Individuals")
  print(Prettable)
  
def print_families_table(family):
  Prettable = PrettyTable()
  Prettable.field_names = ["ID","Marriage Date","Divorce Date","Husband ID","Husband Name","Wife ID","Wife Name","Child IDs","Errors","Anomalies"]
  for f in family:
    Prettable.add_row(f.totalList())
  print("Families")
  print(Prettable)


labels = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

Gedcom_File = open(sys.argv[1], "r") 

individual = []
family = []

def get_individual_by_id(individualId):
  for i in individual:
    if i.Id == individualId:
      return i

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
            individual[len(individual)-1].deathDateObject = deathDate_object
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

# def check_date_before_today_error(date)

# def check_spouse_birth_before_marriage_error(birth_date,marriage_date)

# def check_birth_before_death_error(birth_date,death_date)

#Angie
def check_marriage_before_spouse_death_error(fam):
  husband = get_individual_by_id(fam.husbandId)
  wife = get_individual_by_id(fam.wifeId)
  if husband.alive == False:
    if fam.marriageDateObject > husband.deathDateObject:
      fam.errors.append("Marriage before husband death")
  if wife.alive == False:
    if fam.marriageDateObject > wife.deathDateObject:
      fam.errors.append("Marriage before wife death")

#Liv
# def check_marriage_before_divorce_error(marriage_date,divorce_date)

# def check_divorce_before_spouse_death_error(divorce_date,death_date)

# def check_age_less_than_150_error(age)

# #before death of mother, before 9 months after death of father
# def check_child_birth_before_parents_death_error(child_birth_date,mother_death_date,father_death_date)

# def check_child_birth_before_marriage_anomaly(child_birth_date,marriage_date)

# def check_marriage_after_14_anomaly(wife_birth_date,husband_birth_date,marriage_date)

# #need to make spouse family id an array, discuss args
# def check_no_bigamy_anomaly()

# # individual errors and anomalies
# def check_individual_for_errors_and_anomalies()

# family errors and anomalies
def check_families_for_errors_and_anomalies():
  for fam in family:
    check_marriage_before_spouse_death_error(fam)

populate_gedcom_data(Gedcom_File)
check_families_for_errors_and_anomalies()
print_individuals_table(individual)
print('\n')
print_families_table(family)