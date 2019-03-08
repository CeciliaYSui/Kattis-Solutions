import java.util.Scanner;

public class Chess {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // loop
        char l1, l2;
        int r1, r2;
        for (int i = 0; i < n; i++) {
            l1 = sc.next().charAt(0);
            r1 = sc.nextInt();
            l2 = sc.next().charAt(0);
            r2 = sc.nextInt();
        if(isW(l1,r1)==isW(l2,r2)){
            printpath(l1,r1,l2,r2);
        }
        else System.out.println("Impossible");
        }
    }

    public static void printpath(char l1,int r1,char l2,int r2){
        if(l1==l2 && r1==r2)
            System.out.printf("0 %s %d\n", l1, r1); 
        else if(Math.abs(l1-l2) == Math.abs(r1-r2))
            System.out.printf("1 %s %d %s %d\n", l1, r1, l2, r2); 
        else
            System.out.printf("2 %s %d %s %s %d\n", l1, r1, loc(l1-'A'+1,r1,l2-'A'+1,r2), l2, r2); 
    }

    public static boolean isW(char a, int b){
        if((a-'A'+b)%2==0) return true;
        else return false;
    }

    public static String loc(int l1,int r1,int l2,int r2){
        for (int i = 1; i < 8; i++){
        if(l1+i<=8&&r1+i<=8&&Math.abs(l1+i-l2)==Math.abs(r1+i-r2))
            return Character.toString((char)(l1+i+'A'-1))+" "+Integer.toString(r1+i);
        else if(l1+i<=8&&r1-i>=1&&Math.abs(l1+i-l2)==Math.abs(r1-i-r2))
            return Character.toString((char)(l1+i+'A'-1))+" "+Integer.toString(r1-i);
        else if(l1-i>=1&&r1+i<=8&&Math.abs(l1-i-l2)==Math.abs(r1+i-r2))
            return Character.toString((char)(l1-i+'A'-1))+" "+Integer.toString(r1+i);
        else if(l1-i>=1&&r1-i>=1&&Math.abs(l1-i-l2)==Math.abs(r1-i-r2))
            return Character.toString((char)(l1-i+'A'-1))+" "+Integer.toString(r1-i);
        }
        return ""; 
    }
}