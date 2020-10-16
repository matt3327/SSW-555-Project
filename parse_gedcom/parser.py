from datetime import datetime

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
    self.childFamilyId = ""
    self.childFamilyObject = ""
    self.spouseFamilyIds = []
    self.spouseFamilyObjects = []
    self.errors = []
    self.anomalies = []

  def addSpouseId(self,familyId):
    self.spouseFamilyIds.append(familyId)

  def totalList(self):
    return [self.Id,self.name,self.gender,self.birthDateString,self.age,self.alive,self.deathDateString,self.childFamilyId if len(self.childFamilyId) != 0 else "",self.spouseFamilyIds if len(self.spouseFamilyIds) != 0 else "",self.errors if len(self.errors) != 0 else "",self.anomalies if len(self.anomalies) != 0 else ""]

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
    self.husbandObject = ""
    self.wifeId = ""
    self.wifeName = ""
    self.wifeObject = ""
    self.childrenIds = []
    self.childrenObjects = []
    self.errors = []
    self.anomalies = []

  def addChildId(self,childFamilyId):
    self.childrenIds.append(childFamilyId)
    
  def totalList(self):
    return [self.Id,self.marriageDateString,self.divorceDateString,self.husbandId,self.husbandName,self.wifeId,self.wifeName,self.childrenIds if len(self.childrenIds) != 0 else "",self.errors if len(self.errors) != 0 else "",self.anomalies if len(self.anomalies) != 0 else ""]

labels = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]
individuals = []
families = []

def get_individual_by_id(individualId):
  for i in individuals:
    if i.Id == individualId:
      return i

def get_family_by_id(familyId):
  for f in families:
    if f.Id == familyId:
      return f

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
            individuals[len(individuals)-1].childFamilyId = linelist[2].strip("@")
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
            families[len(families)-1].addChildId(linelist[2].strip("@"))
            
        except:
          pass

def mapObjects():
  for i in individuals:
    i.childFamilyObject = get_family_by_id(i.childFamilyId)
    for spouseFamily in i.spouseFamilyIds:
      i.spouseFamilyObjects.append(get_family_by_id(spouseFamily))
  for f in families:
    f.wifeObject = get_individual_by_id(f.wifeId)
    f.husbandObject = get_individual_by_id(f.husbandId)
    for childId in f.childrenIds:
      f.childrenObjects.append(get_individual_by_id(childId))
