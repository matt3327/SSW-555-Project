from parser import individuals, families
from sprint1_user_stories import *

# individual errors and anomalies
def check_individuals_for_errors_and_anomalies():
  for indiv in individuals:
    US01_check_date_before_today_error(indiv,"Birth")
    US03_check_birth_before_death_error(indiv)
    US07_check_age_less_than_150_error(indiv)
    if indiv.alive == False:
      US01_check_date_before_today_error(indiv,"Death")
    
# family errors and anomalies
def check_families_for_errors_and_anomalies():
  for fam in families:
    husband = get_individual_by_id(fam.husbandId)
    wife = get_individual_by_id(fam.wifeId)
    US01_check_date_before_today_error(fam,"Marriage")
    if fam.divorced == True:
      US01_check_date_before_today_error(fam,"Divorce")
    US05_check_marriage_before_divorce_error(fam)
    US06_check_divorce_before_spouse_death_error(fam)
    US02_birth_before_marriage_error(fam)
    US04_check_marriage_before_spouse_death_error(fam)
    US10_check_marriage_after_14_anomaly(fam)
    for child_id in fam.childrenIds:
      child = get_individual_by_id(child_id)
    US09_check_child_birth_before_marriage_anomaly(fam)
    US08_check_child_birth_before_mother_death_error(fam)