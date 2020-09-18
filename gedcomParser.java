import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class GedcomParser {

    public static ArrayList<Individual> individuals = new ArrayList<Individual>();
    public static ArrayList<Family> families = new ArrayList<Family>();
    
    public static Individual getIndividualById(String id) {
    	for (Individual individual : individuals) {
    		if (individual.getId().equals(id))
    			return individual;
    	}
		return null;
    }
    
    public static Family getFamilyById(String id) {
    	for (Family family : families) {
    		if (family.getId().equals(id))
    			return family;
    	}
		return null;
    }
    
    public class SortIndividuals implements Comparator<Individual> { 
        // sort in ascending order of ids 
        public int compare(Individual a, Individual b) 
        { 
            return a.id.compareTo(b.id); 
        } 
    } 

    public class SortFamilies implements Comparator<Family> { 
        // sort in ascending order of ids 
        public int compare(Family a, Family b) 
        { 
            return a.id.compareTo(b.id); 
        } 
    } 

    public class Individual {
        private final String id;
        private String name;
        private String gender;
        private String birthDate;
        private String deathDate;
        private boolean alive;
        private int age; //never actually used this
        private String childFamilyId;
        private String spouseFamilyId;

        public Individual(final String id) {
            this.id = id;
            this.name = null;
            this.gender = null;
            this.birthDate = null;
            this.deathDate = null;
            this.alive = true;
            this.childFamilyId = null;
            this.spouseFamilyId = null;
            individuals.add(this);
        }

        public String getId() {
            return this.id;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getName() {
            return this.name;
        }

        public void setGender(String gender) {
            this.gender = gender;
        }
        
        public String getGender() {
            return this.gender;
        }

        public void setBirthDate(String birthDate) {
            this.birthDate = birthDate;
        }
        
        public String getBirthDate() {
            return this.name;
        }

        public void setDeathDate(String deathDate) {
            this.deathDate = deathDate;
            this.alive = false;
        }
        
        public String getDeathDate() {
            return this.deathDate;
        }

        public void setChildFamily(String childFamilyId) {
            this.childFamilyId = childFamilyId;
        }
        
        public String getChildFamily() {
            return this.childFamilyId;
        }

        public void setSpouseFamily(String spouseFamilyId) {
            this.spouseFamilyId = spouseFamilyId;
        }
        
        public String getSpouseFamily() {
            return this.spouseFamilyId;
        }

    }

    public class Family {

        private final String id;
        private String husbandId;
        private String husbandName;
        private String wifeId;
        private String wifeName;
        private ArrayList<String> children;
        private String marriedDate;
        private boolean divorced;
        private String divorceDate;

        public Family(final String id) {
            this.id = id;
            this.husbandId = null;
            this.wifeId = null;
            this.children = new ArrayList<String>();
            this.marriedDate = null;
            this.divorced = false;
            this.divorceDate = null;
            families.add(this);
        }
        
        public String getId() {
            return this.id;
        }

        public void setHusbandId(String husbandId) {
            this.husbandId = husbandId;
            // does not work... need work around
            // this.husbandName = individuals.getIndividualById(husbandId).getName();
        }
        
        public String getHusbandId() {
            return this.husbandId;
        }

        //temp work around
        public void setHusbandName(String husbandName) {
            this.husbandName = husbandName;
        }

        public String getHusbandName() {
            return this.husbandName;
        }

        public void setWifeId(String wifeId) {
            this.wifeId = wifeId;
        }

        public String getWifeId() {
            return this.wifeId;
        }
        
        public void setWifeName(String wifeName) {
            this.wifeName = wifeName;
        }

        public String getWifeName() {
            return this.wifeName;
        }

        public void addChildId(String childId) {
            children.add(childId);
        }

        public String getChildrenIds() {
            return children.toString();
        }

        public void setMarriedDate(String marriedDate) {
            this.marriedDate = marriedDate;
            this.divorced = false;
        }

        public String getMarriedDate() {
            return this.marriedDate;
        }

        public void setDivorceDate(String divorceDate) {
            this.divorceDate = divorceDate;
            this.divorced = true;
        }

        public boolean getDivorced() {
            return this.divorced;
        }

    }

    public static void main(String[] args) throws FileNotFoundException {
    	
    	GedcomParser gedcom = new GedcomParser();

        if (args.length == 1) {
            Scanner sc = new Scanner(new File(args[0]));
            String line;
            String[] parts;
            
            //loops through every line in the gedcom file
            while (sc.hasNextLine()) {
                line = sc.nextLine();
                parts = line.split(" ", 3);
                
                // format: 0 <id> <tag>
                // valid tags: INDI or FAM
                if (parts[0].equals("0") && parts.length == 3) {
                    
                	//adds all the properties of an individual until it gets to the next 0
                    if (parts[2].equals("INDI")) {
                    	
                    	String currentId = parts[1];
                    	individuals.add(gedcom.new Individual(currentId));
                    	line = sc.nextLine();
                        parts = line.split(" ", 3); 
                        while (!parts[0].equals("0")) {
                    		if (parts[0].equals("1") && parts.length == 3) {
                    			if (parts[1].equals("NAME"))
                    				getIndividualById(currentId).setName(parts[2]);
                    			else if (parts[1].equals("SEX") && parts[2].matches("M|F")) 
                    				getIndividualById(currentId).setGender(parts[2]);
                    			else if (parts[1].equals("FAMC"))
                    				getIndividualById(currentId).setChildFamily(parts[2]);
                    			else if (parts[1].equals("FAMS"))
                    				getIndividualById(currentId).setSpouseFamily(parts[2]);
                    		}
                    		else if (parts[0].equals("1") && parts.length > 1) {
                    			if (parts[1].equals("BIRTH")) {
                    				line = sc.nextLine();
                                    parts = line.split(" ", 3); 
                                    if (parts.length == 3 && parts[0].equals("2") && parts[1].equals("DATE"))
                                    	getIndividualById(currentId).setBirthDate(parts[2]);
                    			}
                    			//usually of the format 1 DEAT Y - assignment specs say no args
                    			else if (parts[1].equals("DEATH")) {
                    				line = sc.nextLine();
                                    parts = line.split(" ", 3); 
                                    if (parts.length == 3 && parts[0].equals("2") && parts[1].equals("DATE"))
                                    	getIndividualById(currentId).setDeathDate(parts[2]);
                    			}
                    		}
                    		
                    		if (sc.hasNextLine()) {
                    			line = sc.nextLine();
                                parts = line.split(" ", 3); 
                    		}
                    		else
                    			break;
                    	}
                    	
                    }
                    
                    //adds all the properties of a family until it gets to the next 0
                    if (parts[2].equals("FAM")) {
                    	
                    	String currentId = parts[1];
                    	families.add(gedcom.new Family(currentId));
                    	line = sc.nextLine();
                        parts = line.split(" ", 3); 
                        while (!parts[0].equals("0")) {
                    		if (parts[0].equals("1") && parts.length == 3) {
                    			if (parts[1].equals("HUSB")) {
                    				getFamilyById(currentId).setHusbandId(parts[2]);
//                    				getFamilyById(currentId).setHusbandName(getIndividualById(parts[2]).getName());
                    			}
                    			else if (parts[1].equals("WIFE")) {
                    				getFamilyById(currentId).setWifeId(parts[2]);
//                					getFamilyById(currentId).setWifeName(getIndividualById(parts[2]).getName());
                    			}
                    			else if (parts[1].equals("CHIL"))
                    				getFamilyById(currentId).addChildId(parts[2]);
                    		}
                    		else if (parts[0].equals("1") && parts.length > 1) {
                    			if (parts[1].equals("MARR")) {
                    				line = sc.nextLine();
                                    parts = line.split(" ", 3); 
                                    if (parts.length == 3 && parts[0].equals("2") && parts[1].equals("DATE"))
                                    	getFamilyById(currentId).setMarriedDate(parts[2]);
                    			}
                    			else if (parts[1].equals("DIV")) {
                    				line = sc.nextLine();
                                    parts = line.split(" ", 3); 
                                    if (parts.length == 3 && parts[0].equals("2") && parts[1].equals("DATE"))
                                    	getFamilyById(currentId).setDivorceDate(parts[2]);
                    			}
                    		}
                    		
                    		if (sc.hasNextLine()) {
                    			line = sc.nextLine();
                                parts = line.split(" ", 3); 
                    		}
                    		else
                    			break;
                    	}
                    }
                }
            }
            sc.close();
            
            // print ids in order
            // TODO: currently printing odd ones twice, pls fix
            // TODO: not mapping names for families
            // TODO: make it a pretty table
            // see https://github.com/skebir/prettytable

            // Individuals
            Collections.sort(individuals, gedcom.new SortIndividuals());
            StringBuilder individualsTable = new StringBuilder();
            for (Individual individual : individuals) {
                individualsTable.append(individual.getId() + " " 
                		+ individual.getName() + " " 
                		+ individual.getGender() + " " 
                		+ individual.getBirthDate() + " "
                		+ individual.getDeathDate() + " "
                		+ individual.getChildFamily() + " "
                		+ individual.getSpouseFamily() + " "
                		+ "\n");
            }
            System.out.println(individualsTable.toString());

            // Families 
            Collections.sort(families, gedcom.new SortFamilies());
            StringBuilder familiesTable = new StringBuilder();
            for (Family family : families) {
                familiesTable.append(family.getId() + " " 
                + family.getMarriedDate() + " " 
                + family.getDivorced() + " " 
                + family.getHusbandId() + " "
                + family.getHusbandName() + " "
                + family.getWifeId() + " "
                + family.getWifeName() + " "
                + family.getChildrenIds() + " "
                + "\n");
            }
            System.out.println(familiesTable.toString());
            
        }
        
		else {
			throw new IllegalArgumentException("Error: Please provide exactly one GEDCOM file as an argument");
		}
    }
}
