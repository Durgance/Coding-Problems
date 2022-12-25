//{ Driver Code Starts
//Initial Template for Java



import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            inputLine = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);
            int x = Integer.parseInt(inputLine[1]);
            int[] arr = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            Pair ans = new Solve().getFloorAndCeil(arr, n, x);
            System.out.println(ans.floor + " " + ans.ceil);
        }
    }
}

class Pair {
    int floor, ceil;

    Pair() {
        this.floor = 0;
        this.ceil = 0;
    }

    Pair(int floor, int ceil) {
        this.floor = floor;
        this.ceil = ceil;
    }
}

// } Driver Code Ends


//User function Template for Java




class Solve {
    Pair getFloorAndCeil(int[] arr, int n, int x) {
        // code here
        Arrays.sort(arr);
        int value = Arrays.binarySearch(arr,x);
        int floor,ciel;
        if (value !=-1 && value <0){
            floor = (value +1 )*(-1) -1 ;
        }else {
            floor = value;
        }
        if (value !=-1 && value <0){
            ciel = (value +1 )*(-1) ;
        }else {
            ciel = value;
        }
        if (ciel>=arr.length) ciel = -1;
        if (floor == -1){
            Pair pair = new Pair(-1, arr[0]);
            return pair;
        }
        if (ciel == -1){
            Pair pair = new Pair(arr[arr.length-1],-1);
            return pair;
        }
        
        Pair pair = new Pair(arr[floor], arr[ciel]);
        return pair;
    }
}
