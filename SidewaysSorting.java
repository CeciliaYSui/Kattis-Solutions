import java.util.*;

public class SidewaysSorting {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in); 
        int r = sc.nextInt(); 
        while (r != 0){
            int c = sc.nextInt(); 
            sc.nextLine(); 
            ArrayList<String> a = new ArrayList<String>(); 
            for (int m = 0; m < c; m++){
                a.add(""); 
            }
            for (int i = 0; i < r; i++){
                String[] s = sc.nextLine().split("");   // length is c
                for (int j = 0; j < c; j++) {
                    String tmp = a.get(j) + s[j]; 
                    a.set(j,tmp); 
                }
            }
            Collections.sort(a, String.CASE_INSENSITIVE_ORDER);
            
            for (int k = 0; k < r; k++){
                for (int n = 0; n < c; n++){
                    System.out.print(a.get(n).charAt(k)); 
                }
                System.out.println(); 
            }

            r = sc.nextInt(); 
            if (r != 0){
                System.out.println(); 
            }
        }
    }
}