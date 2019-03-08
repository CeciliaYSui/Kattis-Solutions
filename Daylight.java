import java.util.Scanner;

public class Daylight{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        int a, b, c, d; 
        while (sc.hasNextLine()){ 
            System.out.print(sc.next() + " " + sc.next() + " " + sc.next() + " ");
            String[] t1 = sc.next().split(":"); 
            String[] t2 = sc.next().split(":");
            a = Integer.parseInt(t1[0]);
            b = Integer.parseInt(t1[1]); 
            c = Integer.parseInt(t2[0]);
            d = Integer.parseInt(t2[1]);
            if (d >= b){
                System.out.printf("%d hours %d minutes\n",(c-a), (d-b));
            }
            else {
                System.out.printf("%d hours %d minutes\n", (c-a-1), (60-b+d)); 
            }
            sc.nextLine(); 
        }
    }
} 