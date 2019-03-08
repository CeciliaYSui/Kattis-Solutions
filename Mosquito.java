import java.util.Scanner; 

public class Mosquito {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        while (sc.hasNextLine()){
            String[] input = sc.nextLine().split(" "); 
            int M = Integer.parseInt(input[0]); 
            int P = Integer.parseInt(input[1]); 
            int L = Integer.parseInt(input[2]); 
            int E = Integer.parseInt(input[3]); 
            int R = Integer.parseInt(input[4]); 
            int S = Integer.parseInt(input[5]); 
            int N = Integer.parseInt(input[6]); 
            for (int i = 0; i < N; i++){ 
                int oldL = L; 
                L = E * M; // old M 
                M = P / S; // old P 
                P = oldL / R; // old L 
            }
            System.out.println("" + M); 
        }
        sc.close();
    }
}