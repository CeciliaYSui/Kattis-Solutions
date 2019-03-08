import java.util.Scanner;
import java.util.Arrays;  

public class Semafori{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        int N = sc.nextInt(); 
        int L = sc.nextInt();
        int x = 0; // time elapsed 
        int y = 0; // distance 
        int[] arr = new int[3]; 
        sc.nextLine(); 
        for (int ii = 0; ii < N; ii++){
            String s = sc.nextLine();
            Scanner sc2 = new Scanner(s); 
            for (int i = 0; i < 3; i++){
                arr[i] = sc2.nextInt(); 
            }

            x += (arr[0] - y); // prev y
            y = arr[0]; 
            int mid = x % (arr[1] + arr[2]);  
            if ((mid - arr[1]) <= 0) {
                x += (arr[1] - mid); 
            }
        }
        x += (L - arr[0]); 
        System.out.println(x); 
    }
}