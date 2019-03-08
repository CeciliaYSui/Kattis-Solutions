import java.util.Scanner; 

public class Eligibility{
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in); 
        int testcase = Integer.parseInt(sc.nextLine()); 
        String[] portions = new String[4]; 

        for (int i = 0; i < testcase; i++){
            boolean eligibility = true; 
            boolean coach = false; 
            String output; 
            portions = sc.nextLine().split(" "); 
            String[] tmp = portions[1].split("/"); 
            int ed_year = Integer.parseInt(tmp[0]); 
            tmp = portions[2].split("/"); 
            int birth_year = Integer.parseInt(tmp[0]); 
            int courses = Integer.parseInt(portions[3]); 
            if (ed_year >= 2010){
            }
            else if (birth_year >= 1991){
            }
            else if (courses > 40){
                eligibility = false; 
            }
            else {
                coach = true; 
            }

            if (eligibility == false){
                output = " ineligible"; 
            }
            else {
                if (coach == true)
                    output = " coach petitions"; 
                else 
                    output = " eligible"; 
            }
            System.out.println(portions[0] + output);
        }
        sc.close();
    }
}