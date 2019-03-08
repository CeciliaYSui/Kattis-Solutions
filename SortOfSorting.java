import java.util.*;

public class SortOfSorting{
    static final Comparator<String> ORDER = new Comparator<String>(){
        public int compare(String a, String b){
            String aa = a.substring(0, 2); 
            String bb = b.substring(0, 2); 
            return aa.compareTo(bb); 
        }
    }; 
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        int n = sc.nextInt(); 
        sc.nextLine(); 
        while (n != 0){
            ArrayList<String> names = new ArrayList<String>(); 
            for (int i = 0; i < n; i++){
                names.add(sc.nextLine()); 
            }
            Collections.sort(names, ORDER); 
            for (int j = 0; j < n; j++){
                System.out.println(names.get(j)); 
            }
            n = sc.nextInt(); 
            if (n != 0){
                sc.nextLine(); 
                System.out.println(); 
            }
        }       
    }
}