//Angelina Zaccaria Project 02 Submission
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class angieGedcomParser {
	
	public static boolean isInteger(String str) {
		try {
			Integer.parseInt(str);
			return true;
		} catch (NumberFormatException nfe) {
			return false;
		}
	}
	
	public static void main(String[] args) throws FileNotFoundException {
		
		if (args.length == 1) {
			Scanner sc = new Scanner(new File (args[0]));
			String line;
			String[] parts;
			
			while (sc.hasNextLine()) {
				line = sc.nextLine();
				parts = line.split(" ",3);
				
				System.out.println("--> " + line);

				if (parts.length > 1) {
					if (parts[0].equals("0")) {
						
						// format: 0 <id> <tag> 
						// valid tags: INDI or FAM - args not empty
						if (parts.length == 3 && parts[2].matches("INDI|FAM")) {
							System.out.println("<-- 0|" + parts[2] + "|Y|" + parts[1]);
						}
						
						// format: 0 <tag> <arguments that may be ignored> 
						// valid tags: HEAD, TRLR, NOTE
						else if (parts[1].matches("HEAD|TRLR|NOTE")) {
							if (parts.length == 3) {
								System.out.println("<-- 0|" + parts[1] + "|Y|" + parts[2]);
							}
							else {
								System.out.println("<-- 0|" + parts[1] + "|Y");
							}
						}
						
						else {
							if (parts.length == 3) {
								System.out.println("<-- 0|" + parts[1] + "|N|" + parts[2]);
							}
							else {
								System.out.println("<-- 0|" + parts[1] + "|N");
							}
						}	
						
					}
					
					else if (parts[0].equals("1")) {
						
						// format: <level_number> <tag> <arguments>
						
						// valid tags: NAME, FAMC, FAMS, HUSB, WIFE, CHIL - args: not empty
						if (parts[1].matches("NAME|FAMC|FAMS|HUSB|WIFE|CHIL")) {
							if (parts.length == 3) {
								System.out.println("<-- 1|" + parts[1] + "|Y|" + parts[2]);
							}
							else {
								System.out.println("<-- 1|" + parts[1] + "|N");
							}
						}
						
						// valid tags: BIRT, DEAT, MARR, DIV - args: none
						else if (parts[1].matches("BIRT|DEAT|MARR|DIV")) {
							if (parts.length == 2) {
								System.out.println("<-- 1|" + parts[1] + "|Y");
							}
							else {
								System.out.println("<-- 1|" + parts[1] + "|N|" + parts[2]);
							}
						}
						
						// valid tags: SEX - args: M or F
						else if (parts[1].equals("SEX")) {
							if (parts.length == 3 && parts[2].matches("M|F")) {
								System.out.println("<-- 1|" + parts[1] + "|Y|" + parts[2]);
							}
							else {
								System.out.println("<-- 1|" + parts[1] + "|N");
							}
						}
						
						else {
							if (parts.length == 3) {
								System.out.println("<-- 1|" + parts[1] + "|N|" + parts[2]);
							}
							else {
								System.out.println("<-- 1|" + parts[1] + "|N");
							}
						}					
					}
					
					else if (parts[0].equals("2")) {
						
						// format: <level_number> <tag> <arguments>
						// DATE - args: day month year
						if (parts[1].equals("DATE")) {
							if (parts.length == 3) {
								String[] dateFields = parts[2].split(" ");
								if (dateFields.length == 3 &&
										isInteger(dateFields[0]) &&
										isInteger(dateFields[2]) && 
										Integer.parseInt(dateFields[0]) > 0 &&
										(
												(dateFields[1].matches("JAN|MAR|MAY|JUL|AUG|OCT|DEC") && Integer.parseInt(dateFields[0]) < 32) ||
												(dateFields[1].matches("APR|JUN|SEP|NOV") && Integer.parseInt(dateFields[0]) < 31) ||
												(dateFields[1].equals("FEB") && Integer.parseInt(dateFields[0]) < 30)
										) 
									)
								{
									System.out.println("<-- 2|" + parts[1] + "|Y|" + parts[2]);
								}
								else {
									System.out.println("<-- 2|" + parts[1] + "|N|" + parts[2]);
								}
							}
							else {
								System.out.println("<-- 2|" + parts[1] + "|N");
							}
						}
						
						else {
							if (parts.length == 3) {
								System.out.println("<-- 2|" + parts[1] + "|N|" + parts[2]);
							}
							else {
								System.out.println("<-- 2|" + parts[1] + "|N");
							}
						}	
					}
					
					// invalid level (not 0, 1, or 2)
					else {
						if (parts.length == 3) {
							System.out.println("<-- " + parts[0] + "|" + parts[1] + "|N|" + parts[2]);
						}
						else {
							System.out.println("<-- " + parts[0] + "|" + parts[1] + "|N");
						}
					}
				}
				else {
					System.out.println("<-- " + line + "|N");
				}
			}
			sc.close();
		} 
		else {
			throw new IllegalArgumentException("Error: Please provide exactly one GEDCOM file as an argument");
		}
	}
}
