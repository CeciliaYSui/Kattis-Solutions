import java.util.Scanner; 

public class SnapperChain {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in); 
        int t = sc.nextInt(); 
        for (int i = 0; i < t; i++){
            sc.nextLine(); 
            int n = sc.nextInt(); 
            int k = sc.nextInt(); 
            System.out.printf("Case #%d: ", i+1); 
            // signed shifts >>   << 
            // (( (k+1)>>n )  << n ) == (k+1)  ? 
            // if yes "ON", no "OFF"
            System.out.println( (((k+1)>>n)<<n) == (k+1) ? "ON" : "OFF" );
        }				
    }

}