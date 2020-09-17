import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner; 

public class gedcomParser {
    
    
    
    public class Individual {
        private String id;
        private String name;
        private char gender;
        private String birthDate;
        private String deathDate;
        private boolean alive;
        private int age;
        private String childFamilyId;
        private String spouseFamilyId;

        public Individual(String id) {
            this.id = id;
            this.name = null;
            this.gender = null;
            this.birthDate = null;
            this.deathDate = null;
            this.alive = null;
            this.childFamilyId = null;
            this.spouseFamilyId = null;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getName() {
            return this.name;
        }
        
        public void setGender(char gender) {
            this.gender = gender;
        }   

        public void setBirthDate(String birthDate) {
            this.birthDate = birthDate;
            this.alive = true;
        }

        public void setDeathDate(String deathDate) {
            this.deathDate = deathDate;
            this.alive = false;
        }

        public void setChildFamily(String childFamilyId) {
            this.childFamilyId = childFamilyId;
        }

        public void setSpouseFamily(String spouseFamilyId) {
            this.spouseFamilyId = spouseFamilyId;
        }
        
    }

    public class Family {

        private String id;
        private String husbandId;
        private String husbandName;
        private String wifeId;
        private String wifeName;
        private ArrayList<String> children;
        private String marriedDate;
        private boolean divorced;
        private String divorceDate;
        
        public Family(String id) {
            this.id = id;
            this.husbandId = null;
            this.wifeId = null;
            this.children = new ArrayList<String>();
            this.marriedDate = null;
            this.divorced = null;
            this.divorceDate = null;
        }

        public void setHusband(String husbandId) {
            this.husbandId = husbandId;
            // does not work... need work around
            this.husbandName = wifeId.getName();
        }

        public void setWife(String wifeId) {
            this.wifeId = wifeId;
            this.wifeName = wifeId.getName();
        }

        public void addChild(String childId) {
            children.add(childId);
        }

        public void setMarriedDate(String marriedDate){
            this.marriedDate = marriedDate;
            this.divorced = false;
        }

        public void setDivorceDate(String divorceDate) {
            this.divorceDate = divorceDate;
            this.divorced = true;
        }

    }

	public static void main(String[] args) throws FileNotFoundException {
        if (args.length == 1) {
        	Scanner sc = new Scanner(new File(args[0]));
        	
            String[] tags= {"NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"};
            String[] exception = {"INDI", "FAM"};
            

            while (sc.hasNextLine()) {
                StringBuilder output = new StringBuilder();
                String line = sc.nextLine();
                // default is NO
                String incl = "N";
                System.out.println("--> " + line);
                String[] parse = line.split(" ", 3);

                output.append("<-- " + parse[0] + "|");

                if(parse.length == 2){
                    for (String tag : tags){
                        if(tag.equals(parse[1])){
                            incl = "Y";
                        }
                    }
                    output.append(parse[1] + "|" + incl);
                }
                else{
                    for (String tag : tags){
                        if(tag.equals(parse[1])){
                            incl = "Y";
                            output.append(parse[1] + "|" + incl + "|" + parse[2]);
                        }
                    }
    
                    if(incl.equals("N")){
                        for(String except: exception){
                            if(except.equals(parse[2])){
                                incl = "Y";
                                output.append(parse[2] + "|" + incl  + "|" + parse[1]);
                            }
                        }
                        if(incl.equals("N")){
                            output.append(parse[1] + "|" + incl + "|" + parse[2]);
                        }
                    }
                }

                System.out.println(output.toString());

            }
        }

        else{
            System.out.println("Invalid file path");
            System.exit(1);
        }

        

	}

}
