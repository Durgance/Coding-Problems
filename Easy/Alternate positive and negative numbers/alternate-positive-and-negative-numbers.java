//{ Driver Code Starts
//Initial Template for Java



import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            int n = Integer.parseInt(br.readLine().trim());
            int[] arr = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            new Solution().rearrange(arr, n);
            for (int i = 0; i < n; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


//User function Template for Java




class Solution {
    
    
    
    void rearrange(int nums[], int n) {
        Queue<Integer> posQ = new LinkedList<>();
        Queue<Integer> negQ = new LinkedList<>();
        for(int num:nums){
            if (num>=0)posQ.offer(num);
            else negQ.offer(num);
        }
        int k=0;
        while(!posQ.isEmpty() || !negQ.isEmpty()){

            if(!posQ.isEmpty()){

                nums[k] = posQ.remove();

                k++;

            }

            if(!negQ.isEmpty()){

                nums[k] = negQ.remove();

                k++;

            }
            
        }
    }
}