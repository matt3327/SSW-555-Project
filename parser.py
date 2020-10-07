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
    self.divorced = False
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
    
def print_individuals_table():
  Prettable = PrettyTable()
  Prettable.field_names = ["ID","Name","Gender","Birth Date","Age","Alive","Death Date","Child Family","Spouse Families","Errors","Anomalies"]
  for i in individuals:
    Prettable.add_row(i.totalList())
  print("Individuals")
  print(Prettable)
  
def print_families_table():
  Prettable = PrettyTable()
  Prettable.field_names = ["ID","Marriage Date","Divorce Date","Husband ID","Husband Name","Wife ID","Wife Name","Child IDs","Errors","Anomalies"]
  for f in families:
    Prettable.add_row(f.totalList())
  print("Families")
  print(Prettable)


labels = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

# Gedcom_File = open(sys.argv[1], "r") 

individuals = []
families = []

def get_individual_by_id(individualId):
  for i in individuals:
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
        families.append(Family(k[1:-1]))
        Indiv = False
      if k[1] == "I":
        individuals.append(Individual(k[1:-1]))    
        Indiv = True
      findinglabels = True
    elif findinglabels:
      label = linelist[1]
      if Indiv:
        try:
          if label == "NAME":
            individuals[len(individuals)-1].name = " ".join(linelist[2:])
          if label == "SEX":
            individuals[len(individuals)-1].gender = linelist[2]
          if label == "FAMC":
            individuals[len(individuals)-1].childId = linelist[2].strip("@")
          if label == "FAMS":
            individuals[len(individuals)-1].addSpouseId(linelist[2].strip("@"))
          if label == "BIRT":
            lookingBirth = True
          if label == "DEAT":
            lookingDeath = True
          if lookingBirth:
            birthDate_string = " ".join(linelist[2:])
            birthDate_object = datetime.strptime(birthDate_string, '%d %b %Y')
            individuals[len(individuals)-1].birthDateString = birthDate_string
            individuals[len(individuals)-1].birthDateObject = birthDate_object
            individuals[len(individuals)-1].age = str((datetime.now() - birthDate_object)/365).split(" ")[0]
            lookingBirth = False
          if lookingDeath:
            individuals[len(individuals)-1].deathDateString = " ".join(linelist[2:])
            deathDate_object = datetime.strptime(individuals[len(individuals)-1].deathDateString, '%d %b %Y')
            individuals[len(individuals)-1].deathDateObject = deathDate_object
            individuals[len(individuals)-1].age = str((deathDate_object - individuals[len(individuals)-1].birthDateObject)/365).split(" ")[0]
            individuals[len(individuals)-1].alive = False
            lookingDeath = False
        except:
          pass
      else:
        try:
          if lookingMarriage:
            families[len(families)-1].marriageDateString = " ".join(linelist[2:])
            families[len(families)-1].marriageDateObject = datetime.strptime(families[len(families)-1].marriageDateString, '%d %b %Y')
            lookingMarriage = False
          if label == "HUSB":
            hid = linelist[2].strip("@")
            families[len(families)-1].husbandId = hid
            for ind in individuals:
              if ind.Id == hid:
                families[len(families)-1].husbandName = ind.name
          if label == "WIFE":
            wid = linelist[2].strip("@")
            families[len(families)-1].wifeId = wid
            for ind in individuals:
              if ind.Id == wid:       
                families[len(families)-1].wifeName = ind.name 
          if label == "MARR":
            lookingMarriage = True
          if lookingDivorce:
            families[len(families)-1].divorceDateString = " ".join(linelist[2:])
            families[len(families)-1].divorceDateObject = datetime.strptime(families[len(families)-1].divorceDateString, '%d %b %Y')
            families[len(families)-1].divorced = True
            lookingDivorce = False
          if label == "DIV":
            lookingDivorce = True 
          if label == "CHIL":
            families[len(families)-1].addChild(linelist[2].strip("@"))
            
        except:
          pass

def US01_check_date_before_today_error(indiv_or_fam,identifier):
  if identifier == "Birth":
    dateObject = indiv_or_fam.birthDateObject
  elif identifier == "Death":
    dateObject = indiv_or_fam.deathDateObject
  elif identifier == "Marriage":
    dateObject = indiv_or_fam.marriageDateObject
  elif identifier == "Divorce":
    dateObject = indiv_or_fam.divorceDateObject
  if datetime.now() < dateObject:
      indiv_or_fam.errors.append(identifier + " date is after current date")

# birth/death dates for individual
# marriage/divorce dates for families



# def US02_check_spouse_birth_before_marriage_error(fam,husband,wife):

def US03_check_birth_before_death_error(indiv):
  if indiv.alive == False and indiv.birthDateObject > indiv.deathDateObject:
    indiv.errors.append("Death date is before birth date")

#Angie-US04
def US04_check_marriage_before_spouse_death_error(fam,husband,wife):
  if husband.alive == False:
    if fam.marriageDateObject > husband.deathDateObject:
      fam.errors.append("Marriage date is after husband death date")
  if wife.alive == False:
    if fam.marriageDateObject > wife.deathDateObject:
      fam.errors.append("Marriage date is after wife death date")

#Liv-US05
def US05_check_marriage_before_divorce_error(fam):
  if fam.divorced == True:
    if fam.marriageDateObject > fam.divorceDateObject:
      fam.errors.append("Divorce date is before marriage date")

#Liv-US06
def US06_check_divorce_before_spouse_death_error(fam,husband,wife):
  if fam.divorced == True:
    if husband.alive == False:
      if fam.divorceDateObject > husband.deathDateObject:
        fam.errors.append("Divorce date is after husband death date")
    if wife.alive == False:
      if fam.divorceDateObject > wife.deathDateObject:
        fam.errors.append("Divorce date is after wife death date")


#Jenn-US07
def US07_check_age_less_than_150_error(indiv):
  if int(indiv.age) > 150: 
    indiv.errors.append("Individual age greater than 150")

# #before death of mother, before 9 months after death of father

#def US08_check_child_birth_before_parents_death_error(fam,husband,wife,child):

#Jenn-US09
def US09_check_child_birth_before_marriage_anomaly(fam,child):
  if fam.marriageDateObject > child.birthDateObject: #marriage after birth
    fam.anomalies.append(child.Id + " born before parents married")

# def US10_check_marriage_after_14_anomaly(fam,husband,wife):

# def US11_check_no_bigamy_anomaly(indiv):

# need to add a US12

# individual errors and anomalies
def check_individuals_for_errors_and_anomalies():
  for indiv in individuals:
    US01_check_date_before_today_error(indiv,"Birth")
    US03_check_birth_before_death_error(indiv)
    US07_check_age_less_than_150_error(indiv)
    if indiv.alive == False:
      US01_check_date_before_today_error(indiv,"Death")
    # US03_check_birth_before_death_error(indiv)
    
# family errors and anomalies
def check_families_for_errors_and_anomalies():
  for fam in families:
    husband = get_individual_by_id(fam.husbandId)
    wife = get_individual_by_id(fam.wifeId)
    child = get_individual_by_id(child)
    US01_check_date_before_today_error(fam,"Marriage")
    if fam.divorced == True:
      US01_check_date_before_today_error(fam,"Divorce")
    # US02_check_spouse_birth_before_marriage_error(fam,husband,wife)
    US04_check_marriage_before_spouse_death_error(fam,husband,wife)
    US05_check_marriage_before_divorce_error(fam)
    US06_check_divorce_before_spouse_death_error(fam, husband, wife)
    for child in fam.children:
      US09_check_child_birth_before_marriage_anomaly(fam,child)

# populate_gedcom_data(Gedcom_File)
# check_families_for_errors_and_anomalies()
# print_individuals_table(individual)
# print('\n')
# print_families_table(family)

if __name__ == "__main__":
    Gedcom_File = open(sys.argv[1], "r") 
    populate_gedcom_data(Gedcom_File)
    check_individuals_for_errors_and_anomalies()
    check_families_for_errors_and_anomalies()
    check_individual_for_errors_and_anomalies()
    print_individuals_table()
    print('\n')
    print_families_table()
