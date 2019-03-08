import java.util.*; 

class ORDER implements Comparator<String[]> { 
    int id; 
    public void set_id(int i){
        this.id = i; 
    }
    public int compare(String[] a, String[] b) { 
        String aa = a[this.id]; 
        String bb = b[this.id];  
        return aa.compareTo(bb); 
    } 
} 

public class MusicYourWay{
    public static void main(String[] args){
        // input 
        Scanner sc = new Scanner(System.in); 
        String[] attri = sc.nextLine().split(" "); 
        int m = sc.nextInt(); 
        sc.nextLine(); 
        ArrayList<String[]> songs = new ArrayList<String[]> (); 
        for (int i = 0; i<m; i++){
            songs.add(sc.nextLine().split(" ")); 
        }
        int n = sc.nextInt(); 
        sc.nextLine(); 
        for (int j = 0; j < n; j++) {
            String comp = sc.nextLine(); 
            for (String a : attri){
                System.out.print(a + " "); 
            }
            System.out.println(); 
            int tmp = 0; 
            for (int k = 0; k < attri.length; k++){
                if (comp.equals(attri[k])){
                    tmp = k; 
                    break;
                }
            }  
            ORDER sortby = new ORDER(); 
            sortby.set_id(tmp);
            Collections.sort(songs, sortby);  
            for (int l = 0; l < m; l++){
                String[] s = songs.get(l); 
                for (int p = 0; p < attri.length; p++){
                    System.out.print(s[p] + " "); 
                }
                System.out.println(); 
            }
            if (j != n-1){
                System.out.println(); 
            }

        }         
    }
}
