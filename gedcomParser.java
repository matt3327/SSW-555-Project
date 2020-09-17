// Olivia Powers SSW 555 Project 02
package Project02;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner; 

public class gedcomParser {

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
