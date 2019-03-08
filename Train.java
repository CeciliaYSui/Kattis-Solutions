import java.util.Scanner; 

public class Train {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        int c = sc.nextInt(); 
        int n = sc.nextInt(); 
        sc.nextLine(); 
        boolean x = true; 
        int on = 0; 

        for (int ii = 0; ii < n; ii++){
            String[] input = sc.nextLine().split(" ");  
            int[] a = new int[3]; 
            for(int i = 0; i < 3; i++)
                a[i] = Integer.parseInt(input[i]);  
            if (ii==0){
                if ((a[0]!=0) || (a[1]>c))
                    x = false; 
                on += a[1]; 
                if ((on < c) && (a[2]!=0))
                    x = false;
            }
            else if (ii == (n-1)){
                if ((a[0]!=on) || (a[1]!=0) || (a[2]!=0))
                    x = false;
            }
            else {
                if (a[0] > on)
                    x = false;
                on -= a[0]; 
                if (a[1] > (c-on))
                    x = false; 
                on += a[1]; 
                if ((on < c) && (a[2]!=0))
                    x = false;
            }
        }

        if (x)
            System.out.println("possible"); 
        else 
            System.out.println("impossible"); 
    }
}