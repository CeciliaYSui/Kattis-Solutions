import java.util.Scanner; 
import java.util.Stack; 

public class ContestScoring{
    public static void main(String[] arsgs){
        Scanner sc = new Scanner(System.in); 
        String input = sc.nextLine(); 
        String[] record = new String[3]; 
        String[] letter = new String[100]; 
        int cnt = 0; 
        int time = 0; 
        Stack <String> s = new Stack<String>(); 


        while (!input.equals("-1")){  
            record = input.split(" "); 
            if (record[2].equals("right")){
                letter[cnt] = record[1];    // store the letter for right problem
                cnt++;  // no of right 
                time += Integer.parseInt(record[0]); // right time 
                while ( !s.empty() && (s.peek().equals(record[1])) ){
                    time += 20; 
                    s.pop(); 
                }
            }
            else
                s.push(record[1]); // problem letter  
            input = sc.nextLine(); 
        }
        while (!s.empty()){
            String check = s.peek(); 
            for(int i = 0; i <= cnt; i++){
                if(check.equals(letter[i])){
                    time += 20; 
                }
            }
            s.pop(); 
        }
        System.out.println("" + cnt + " " + time); 
        sc.close(); 
    }
}