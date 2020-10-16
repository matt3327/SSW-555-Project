import sys
from parser import *
from implement_user_stories import *
from print_tables import *

Gedcom_File = open(sys.argv[1], "r") 
populate_gedcom_data(Gedcom_File)
mapObjects()
check_individuals_for_errors_and_anomalies()
check_families_for_errors_and_anomalies()
print_individuals_table()
print_families_table()
