import java.util.Scanner; 

public class LeftBeehind {
    public static void main (String[] args){
        Scanner sc = new Scanner (System.in); 
        String line = sc.nextLine(); 
        while(!line.equals("0 0")){
            String[] input = line.split(" "); 
            int sweet = Integer.parseInt(input[0]); 
            int sour = Integer.parseInt(input[1]); 
            if ((sweet + sour) == 13)
                System.out.println("Never speak again."); 
            else if (sweet < sour)
                System.out.println("Left beehind."); 
            else if (sweet > sour)
                System.out.println("To the convention."); 
            else 
                System.out.println("Undecided.");
            line = sc.nextLine(); 
        }
        sc.close();
    }
}