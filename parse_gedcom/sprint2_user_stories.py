# US11 - Jenn

# US12 - Jenn
def US12_check_child_birth_after_divorce_anomaly(fam):
  for child in fam.childrenObjects:
    if fam.divorceDateObject < child.birthDateObject: #divorce before birth
      fam.anomalies.append(child.Id + " born after parents divorced")    
# US13 - Justin

# US14 - Justin

# US15 - Matt

# US16 - Matt

# US17 - Liv

# US18 - Liv

# US19 - Angie

# US20 - Angie
