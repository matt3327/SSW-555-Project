# US11 - Jenn

# US12 - Jenn- no more than 9 months after divorce
def US12_check_child_birth_after_divorce_anomaly(fam):
  if fam.divorced == True:
    for child in fam.childrenObjects: 
      if (((child.birthDateObject-fam.divorceDateObject).days)/30) > 9:
        fam.anomalies.append(child.Id + " born over 9 months after parents divorced")    
# US13 - Justin

# US14 - Justin

# US15 - Matt

# US16 - Matt

# US17 - Liv

# US18 - Liv

# US19 - Angie

# US20 - Angie
