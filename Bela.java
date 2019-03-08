import java.util.Scanner; 

public class Bela {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        int N = sc.nextInt(); 
        char dom = sc.next().charAt(0); 
        int sum = 0; 
        for (int ii = 0; ii < 4*N; ii++){
            String input = sc.next(); 
            char a = input.charAt(0);
            char b = input.charAt(1);  
            if (a == 'J'){
                if (b == dom)
                    sum += 20;
                else 
                    sum += 2;  
            }
            else if (a == '9'){
                if (b == dom)
                    sum += 14; 
            }
            else {
                switch(a){
                    case 'A':
                        sum += 11; 
                        break;
                    case 'K':
                        sum += 4;
                        break; 
                    case 'Q':
                        sum += 3; 
                        break;
                    case 'T':
                        sum += 10; 
                        break;
                    default:
                        break;
                }
            }
        }
        System.out.println(sum); 
    }
}