from datetime import datetime

# Justin
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

# Justin
def US02_birth_before_marriage_error(fam):
  if fam.marriageDateObject < fam.husbandObject.birthDateObject or fam.marriageDateObject < fam.wifeObject.birthDateObject:
    fam.errors.append("Marriage occured before birth date")
  
# Angie
def US03_check_birth_before_death_error(indiv):
  if indiv.alive == False and indiv.birthDateObject > indiv.deathDateObject:
    indiv.errors.append("Death date is before birth date")

# Angie
def US04_check_marriage_before_spouse_death_error(fam):
  if fam.husbandObject.alive == False:
    if fam.marriageDateObject > fam.husbandObject.deathDateObject:
      fam.errors.append("Marriage date is after husband death date")
  if fam.wifeObject.alive == False:  
    if fam.marriageDateObject > fam.wifeObject.deathDateObject:
      fam.errors.append("Marriage date is after wife death date")

# Liv
def US05_check_marriage_before_divorce_error(fam):
  if fam.divorced == True:
    if fam.marriageDateObject > fam.divorceDateObject:
      fam.errors.append("Divorce date is before marriage date")

# Liv
def US06_check_divorce_before_spouse_death_error(fam):
  if fam.divorced == True:
    if fam.husbandObject.alive == False:
      if fam.divorceDateObject > fam.husbandObject.deathDateObject:
        fam.errors.append("Divorce date is after husband death date")
    if fam.wifeObject.alive == False:
      if fam.divorceDateObject > fam.wifeObject.deathDateObject:
        fam.errors.append("Divorce date is after wife death date")

# Jenn
def US07_check_age_less_than_150_error(indiv):
  if int(indiv.age) > 150: 
    indiv.errors.append("Individual age greater than 150")

# Matt
def US08_check_child_birth_before_mother_death_error(fam):
  for child in fam.childrenObjects:
    if fam.wifeObject.alive == False and fam.wifeObject.deathDateObject < child.birthDateObject:  
      fam.errors.append("Child born after death of mother")

# Jenn
def US09_check_child_birth_before_marriage_anomaly(fam):
  for child in fam.childrenObjects:
    if fam.marriageDateObject > child.birthDateObject: #marriage after birth
      fam.anomalies.append(child.Id + " born before parents married")    

# Matt
def US10_check_marriage_after_14_anomaly(fam):
  day1 = fam.wifeObject.birthDateObject
  day2 = fam.marriageDateObject 
  day3 = (((day2 - day1).days)/365)
  day4 = fam.husbandObject.birthDateObject
  day5 = fam.marriageDateObject 
  day6 = (((day5 - day4).days)/365)
  if day3 < 14:
    fam.anomalies.append("Wife married before 14 anomaly")
  if day6 < 14:
    fam.anomalies.append("Husband married before 14 anomaly")
  # if int(wife.birthDateObject) - int(fam.marriageDateObject) > 14 and int(husband.birthDateObject) - int(fam.marriageDateObject) >14:
  #   fam.errors.append("error marriage before 14")