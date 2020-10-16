from prettytable import PrettyTable
# from parser import individuals, families

def print_individuals_table():
  Prettable = PrettyTable()
  Prettable.field_names = ["ID","Name","Gender","Birth Date","Age","Alive","Death Date","Child Family","Spouse Families","Errors","Anomalies"]
  for i in individuals:
    Prettable.add_row(i.totalList())
  print("Individuals")
  print(Prettable, "\n")
  
def print_families_table():
  Prettable = PrettyTable()
  Prettable.field_names = ["ID","Marriage Date","Divorce Date","Husband ID","Husband Name","Wife ID","Wife Name","Child IDs","Errors","Anomalies"]
  for f in families:
    Prettable.add_row(f.totalList())
  print("Families")
  print(Prettable, "\n")
