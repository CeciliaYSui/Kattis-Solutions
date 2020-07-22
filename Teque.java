// Java Implementation --> Python speed limit *
import java.util.*;
import java.io.*;
public class Teque {
    private static HashMap<Integer, Integer> df = new HashMap<>();
    private static HashMap<Integer, Integer> db = new HashMap<>();
    static int fmin, fmax, bmin, bmax = 0; 

    public static void main(String[] args) throws IOException{
        // Scanner sc = new Scanner(System.in); // I/O too slow??? 
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        // StringTokenizer st; 

        int n = Integer.parseInt(sc.readLine());
        for (int i = 0; i < n; i++) {
            String[] act = sc.readLine().split(" ");
            int val = Integer.parseInt(act[1]); 
            int tmp; 
            if (act[0].charAt(0) == 'p') {
                switch(act[0].charAt(5)) {
                    case 'b':
                        db.put(bmax, val);
                        bmax++;
                        break;
                    case 'f':
                        fmin--;
                        df.put(fmin, val);
                        break;
                    default: // push_middle
                        if (df.size() == db.size()) {
                            bmin--;
                            db.put(bmin, val);
                        }
                        else {
                            df.put(fmax, db.get(bmin));
                            fmax++;
                            db.put(bmin, val);
                        }
                }
                // clean up 
                if (df.size() > db.size()) {
                    bmin--;
                    fmax--;
                    db.put(bmin, df.get(fmax));
                    df.remove(fmax);
                }
                else if (db.size() > df.size()+1) {
                    df.put(fmax, db.get(bmin));
                    db.remove(bmin);
                    bmin++;
                    fmax++;
                }
            }
            else {
                if (val < fmax - fmin){
                    tmp = df.get(fmin + val); 
                }
                else {
                    val -= fmax - fmin; 
                    tmp = db.get(bmin + val); 
                }
                out.write(Integer.toString(tmp) + "\n"); 
                //System.out.println(tmp); 
            }
        }
        out.flush(); 
    }
}