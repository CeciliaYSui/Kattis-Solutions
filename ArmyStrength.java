import java.util.*; 

public class ArmyStrength {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        int N = sc.nextInt(); 
        sc.nextLine(); 
        for (int ii = 0; ii < N; ii++){
            sc.nextLine(); 
            String[] input = sc.nextLine().split(" "); 
            int G = Integer.parseInt(input[0]); 
            int M = Integer.parseInt(input[1]); 
            String[] Ginput = sc.nextLine().split(" ");
            int[] Garr = new int[G]; 
            for (int i = 0; i < G; i++){
                Garr[i] = Integer.parseInt(Ginput[i]);
            }
            String[] Minput = sc.nextLine().split(" "); 
            int[] Marr = new int[M]; 
            for (int j = 0; j < M; j++){
                Marr[j] = Integer.parseInt(Minput[j]); 
            }
            Arrays.sort(Garr);
            Arrays.sort(Marr); 
            if (Garr[G-1] >= Marr[M-1]){
                System.out.println("Godzilla"); 
            }
            else {
                System.out.println("MechaGodzilla"); 
            }
        }
        sc.close(); 
    }
}