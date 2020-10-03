import org.junit.Test;
import static org.junit.Assert.*;


//  import GedcomParser;
//  import GedcomParser.Family;
//  import GedcomParser.Family.setMarriedDate;
//  import GedcomParser.Family.setDivorceDate;
//  import GedcomParser.Family.validMarriageDivorceDate;



public class TestMarriageBeforeDivorce extends GedcomParser {

    @Test
    public void TestMarriageDivorce() {
        Family fam1 = new Family("fam1");
        fam1.setMarriedDate("3 OCT 1999");
        fam1.setDivorceDate("5 NOV 1998");
        assertTrue(fam1.validMarriageDivorceDate());
    }
    public static void main(String[] args) {
    }
    
}


