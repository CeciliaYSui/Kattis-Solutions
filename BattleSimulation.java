import java.util.Scanner;
import java.util.Arrays;

public class BattleSimulation{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        String input = sc.nextLine() + "   "; 
        int start = 0; 
        int end = 3; 
        for (int i = 0; i < input.length()-2; i++){
            if (end > input.length() + 1){
                break;
            }
            if (input.substring(start, end).equals("RBL") || 
                input.substring(start, end).equals("RLB") || 
                input.substring(start, end).equals("BLR") ||
                input.substring(start, end).equals("BRL") || 
                input.substring(start, end).equals("LBR") ||
                input.substring(start, end).equals("LRB")){
                System.out.print("C"); 
                start += 3; 
                end += 3; 
            }
            else {
                if (input.charAt(start) == 'R')
                    System.out.print("S");     
                else if (input.charAt(start) == 'B')
                    System.out.print("K"); 
                else if (input.charAt(start) == 'L')
                    System.out.print("H"); 
                else {
                    break;
                }
                start++; 
                end++; 
            }
        }
        sc.close();
    }
}