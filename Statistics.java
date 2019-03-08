import java.util.Scanner; 

public class Statistics {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        int cnt = 1; 
        while (sc.hasNextLine()){
            String input = sc.nextLine(); 
            String[] line = input.split(" "); 
            int[] sample = new int[line.length-1]; 
            for (int ii = 0; ii < line.length -1; ii++){
                sample[ii] = Integer.parseInt(line[ii + 1]); 
            }
            int range = getMax(sample) - getMin(sample); 
            System.out.printf("Case %d: %d %d %d\n", cnt, getMin(sample), getMax(sample), range); 
            cnt++; 
        }
        sc.close();
    }

    public static int getMax(int[] arr){ 
        int max = arr[0]; 
        for(int i=1;i < arr.length;i++){ 
            if(arr[i] > max)
                max = arr[i]; 
        } 
        return max; 
    }
     
    public static int getMin(int[] arr){ 
        int min = arr[0]; 
        for(int i=1;i<arr.length;i++){ 
            if(arr[i] < min)
                min = arr[i]; 
        } 
        return min; 
    } 
}