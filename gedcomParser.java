import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class GedcomParser {

    // holds all individuals and families
    public static ArrayList<Individual> individuals = new ArrayList<Individual>();
    public static ArrayList<Family> families = new ArrayList<Family>();
    
    // takes in Id and returns the Individual that corresponds
    public static Individual getIndividualById(String id) {
        // iterates through all individuals in the individuals array
    	for (Individual individual : individuals) {
    		if (individual.getId().equals(id))
    			return individual;
        }
        // if no such individual matches return null
		return null;
    }
    
    // takes in family Id and returns Family that corresponds
    public static Family getFamilyById(String id) {
        // iterates through all families in the family array
    	for (Family family : families) {
    		if (family.getId().equals(id))
    			return family;
        }
        // if no such family matches return null
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

    // making of an individual
    public class Individual {

        //characteristics
        private final String id;
        private String name;
        private String gender;
        private String birthDate;
        private String deathDate;
        private boolean alive;
        private int age; //never actually used this
        private String childFamilyId;
        private String spouseFamilyId;

        // instantiating an individual
        public Individual(final String id) {
            this.id = id;
            this.name = null;
            this.gender = null;
            this.birthDate = null;
            this.deathDate = null;
            this.alive = true;
            this.childFamilyId = null;
            this.spouseFamilyId = null;
            // once individual is created, then added to the array of individuals
            individuals.add(this);
        }

        // getters and setters

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
            return this.birthDate;
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

    // making  of a family
    public class Family {

        //characteristics
        private final String id;
        private String husbandId;
        private String husbandName;
        private String wifeId;
        private String wifeName;
        private ArrayList<String> children;
        private String marriedDate;
        private boolean divorced;
        private String divorceDate;

        // instantion of a family
        public Family(final String id) {
            this.id = id;
            this.husbandId = null;
            this.husbandName = null;
            this.wifeId = null;
            this.wifeName = null;
            this.children = new ArrayList<String>();
            this.marriedDate = null;
            this.divorced = false;
            this.divorceDate = null;
            families.add(this);
        }

        // getters and setters
        
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
        
        // create to call families and individuals
    	GedcomParser gedcom = new GedcomParser();

        if (args.length == 1) {
            Scanner sc = new Scanner(new File(args[0]));
            String line = null;
            String[] parts = null;

            if (sc.hasNextLine()) {
                line = sc.nextLine();
                parts = line.split(" ", 3);
            }
            
            //loops through every line in the gedcom file
            while (sc.hasNextLine()) {
                // if (sc.hasNextLine()) {
                //     line = sc.nextLine();
                //     parts = line.split(" ", 3); 
                // }
                // // breaks out of loop when no other lines
                // else
                //     break;

                // format: 0 <id> <tag>
                // valid tags: INDI or FAM
                if (parts[0].equals("0") && parts.length == 3) {

                	//adds all the properties of an individual until it gets to the next 0
                    if (parts[2].equals("INDI")) {
                    	
                        String currentId = parts[1];
                        //creates individual and adds it to the array
                        individuals.add(gedcom.new Individual(currentId));
                        line = sc.nextLine();
                        parts = line.split(" ", 3); 
                        
                        // while INDI or FAM line not apparent
                        while (!parts[0].equals("0")) {
                            // line = sc.nextLine();
                            // parts = line.split(" ", 3); 

                            // searches through array to get relevant individual and sets accordingly
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
                            
                            // sets birth or death
                            if (parts[1].equals("BIRT")) {
                                line = sc.nextLine();
                                parts = line.split(" ", 3); 

                                if (parts[0].equals("2") && parts[1].equals("DATE")){
                                    getIndividualById(currentId).setBirthDate(parts[2]);
                                }
                            }
                            //usually of the format 1 DEAT Y - assignment specs say no args
                            if (parts[1].equals("DEAT")) {
                                line = sc.nextLine();
                                parts = line.split(" ", 3); 
                                
                                if (parts[0].equals("2") && parts[1].equals("DATE"))
                                    getIndividualById(currentId).setDeathDate(parts[2]);

                            }
                            
                            // looks at the next line in the document
                    		if (sc.hasNextLine()) {
                                line = sc.nextLine();
                                parts = line.split(" ", 3); 
                            }
                            // breaks out of loop when no other lines
                    		else
                    		    break;
                    	}
                    	
                    }
                    
                    //adds all the properties of a family until it gets to the next 0
                    else if (parts[2].equals("FAM")) {
                    	
                        String currentId = parts[1];
                        //creates family and adds it to the array
                    	families.add(gedcom.new Family(currentId));
                    	line = sc.nextLine();
                        parts = line.split(" ", 3); 
                        // not a family or individual
                        while (!parts[0].equals("0")) {
                            // adding husband, wife, child to family
                    		if (parts[0].equals("1") && parts.length == 3) {
                    			if (parts[1].equals("HUSB")) {
                    				getFamilyById(currentId).setHusbandId(parts[2]);
                   				    getFamilyById(currentId).setHusbandName(getIndividualById(parts[2]).getName());
                    			}
                    			else if (parts[1].equals("WIFE")) {
                    				getFamilyById(currentId).setWifeId(parts[2]);
               					    getFamilyById(currentId).setWifeName(getIndividualById(parts[2]).getName());
                    			}
                    			else if (parts[1].equals("CHIL"))
                    				getFamilyById(currentId).addChildId(parts[2]);
                            }
                            // adding married and divorced information
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
                    		
                    		// looks at the next line in the document
                    		if (sc.hasNextLine()) {
                    			line = sc.nextLine();
                                parts = line.split(" ", 3); 
                            }
                            // breaks out of loop when no other lines
                    		else
                    			break;
                    	}
                    }
                    else {
                        if (sc.hasNextLine()) {
                            line = sc.nextLine();
                            parts = line.split(" ", 3); 
                        }
                        // breaks out of loop when no other lines
                        else
                            break;
                    }
                }
                else {
                    if (sc.hasNextLine()) {
                        line = sc.nextLine();
                        parts = line.split(" ", 3); 
                    }
                    // breaks out of loop when no other lines
                    else
                        break;
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
                individualsTable.append(individual.getId() + "\t" 
                		+ individual.getName() + "\t" 
                		+ individual.getGender() + "\t" 
                		+ individual.getBirthDate() + "\t"
                		+ individual.getDeathDate() + "\t"
                		+ individual.getChildFamily() + "\t"
                		+ individual.getSpouseFamily() + "\n");
            }
            System.out.println("indiv id\tname\tgender\tbirth date\tdeath date\tFAMC\tFAMS");
            System.out.println(individualsTable.toString());

            // Families 
            Collections.sort(families, gedcom.new SortFamilies());
            StringBuilder familiesTable = new StringBuilder();
            for (Family family : families) {
                familiesTable.append(family.getId() + "\t" 
                + family.getMarriedDate() + "\t" 
                + family.getDivorced() + "\t" 
                + family.getHusbandId() + "\t"
                + family.getHusbandName() + "\t"
                + family.getWifeId() + "\t"
                + family.getWifeName() + "\t"
                + family.getChildrenIds() + "\n");
            }
            System.out.println("fam id\tmarriage date\tdivorced?\thusband id\thusband name\twife id\twife name\tchildren ids");
            System.out.println(familiesTable.toString());
            
        }
        
		else {
			throw new IllegalArgumentException("Error: Please provide exactly one GEDCOM file as an argument");
		}
    }
}
