import java.util.Scanner; 

public class DST{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); 
        sc.nextLine(); 
        for (int ii = 0; ii < n; ii++){
            String s = sc.nextLine();
            Scanner sc2 = new Scanner(s); 
            char a = sc2.next().charAt(0); 
            int D = sc2.nextInt(); 
            int H = sc2.nextInt(); 
            int M = sc2.nextInt(); 
            int Dmin = D%60;  // min 
            int Dhr = D/60;   // hour <=2
            if (a == 'F'){
                if (Dhr == 0){
                    if (Dmin+M >= 60){
                        if (H == 23){
                            H = -1; 
                        }
                        System.out.println((H+1) + " " + (Dmin+M-60));
                    }
                    else{
                        System.out.println(H + " " + (Dmin+M));
                    }   
                }
                else if (Dhr == 1){
                    H += 1; 
                    if (Dmin+M >= 60){
                        if (H < 23){
                            System.out.println((H+1) + " " + (Dmin+M-60));
                        }
                        else {
                            System.out.println((H+1-24) + " " + (Dmin+M-60));
                        }
                    }
                    else{ 
                        if (H == 24){
                            H = 0; 
                        }
                        System.out.println(H + " " + (Dmin+M));
                    }
                }
                else {
                    if (H+2 < 24) {
                        System.out.println((H+2) + " " + M);}
                    else {
                        System.out.println((H+2-24) + " " + M);} 
                }
            }
            else {  // a == 'B'
                if (Dhr == 0){
                    if (Dmin <= M)
                            System.out.println(H + " " + (M-Dmin)); 
                    else {
                        if (H == 0){
                            H = 24; 
                        }
                        System.out.println((H-1) + " " + (60-Dmin+M));
                    }
                }    
                else if (Dhr == 1){
                    if (H == 0){
                        H = 24; 
                    }
                    H -= 1; 
                    if (Dmin <= M){
                        System.out.println(H + " " + (M-Dmin));
                    }
                    else {
                        if (H == 0){
                            H = 24; 
                        }
                        System.out.println((H-1) + " " + (60-Dmin+M));
                    }      
                }
                else {
                    if (H-2 > 0){
                        System.out.println((H-2) + " " + M);
                    }
                    else {
                        System.out.println((24+H-2) + " " + M); 
                    }
                }
            }
        }
    }
}

