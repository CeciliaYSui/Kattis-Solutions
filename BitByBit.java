import java.util.*;

public class BitByBit {
    public static char OR (char i, char j) {
        if (i == '1' || j == '1')
            return '1';
        else if (i == '?' || j == '?')
            return '?'; 
        else 
            return '0'; 
    }
    public static char AND(char a, char b){
        if (a == '0' || b == '0')
            return '0'; 
        else if (a == '?' || b == '?')
            return '?'; 
        else 
            return '1'; 
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); 
        while (n != 0){
            sc.nextLine(); 
            char[] bits = new char[32]; 
            for (int ii = 32; ii --> 0;){
                bits[ii] = '?'; 
            }
            while (n --> 0) {
                char c = sc.next().charAt(0); 
                if (c == 'C')
                   bits[sc.nextInt()] = '0'; 
                else if (c == 'S')
                    bits[sc.nextInt()] = '1'; 
                else if (c == 'O'){
                    int i = sc.nextInt(); 
                    bits[i] = OR(bits[i], bits[sc.nextInt()]); 
                }
                else if (c == 'A'){
                    int i = sc.nextInt(); 
                    bits[i] = AND(bits[i], bits[sc.nextInt()]); 
                }
            }
        System.out.println(new StringBuilder(new String(bits)).reverse());
        n = sc.nextInt(); 
    }
}
}