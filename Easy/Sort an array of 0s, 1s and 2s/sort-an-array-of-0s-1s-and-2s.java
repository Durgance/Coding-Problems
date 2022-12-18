//{ Driver Code Starts
//Initial template for Java

import java.io.*;
import java.util.*;


// } Driver Code Ends
//User function template for Java

class Solution
{
    public static void sort012(int nums[], int n)
    {
        int zeroCount = 0;
        int oneCount = 0;
        int twoCount = 0;
        for(int num:nums){
            if (num==0) zeroCount++;
            else if (num==1) oneCount++;
            else if (num==2) twoCount++;
            // else if (num==0) zeroCount++;
        }int i=0;
        while(zeroCount-->0){
            nums[i]=0;
            i++;
        }
        while(oneCount-->0){
            nums[i]=1;
            i++;
        }
        while(twoCount-->0){
            nums[i]=2;
            i++;
        } 
    }
}

//{ Driver Code Starts.

class GFG {
    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
        while(t-->0){
            int n = Integer.parseInt(br.readLine().trim());
            int arr[] = new int[n];
            String inputLine[] = br.readLine().trim().split(" ");
            for(int i=0; i<n; i++){
                arr[i] = Integer.parseInt(inputLine[i]);
            }
            Solution ob=new Solution();
            ob.sort012(arr, n);
            StringBuffer str = new StringBuffer();
            for(int i=0; i<n; i++){
                str.append(arr[i]+" ");
            }
            System.out.println(str);
        }
    }
}


// } Driver Code Ends