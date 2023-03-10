//{ Driver Code Starts
import java.io.*;
import java.util.*;
import java.util.stream.*;

class Array {
    
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
		
		while(t-->0){
		    
		    //input size of array
		    int n = Integer.parseInt(br.readLine().trim());
		    int arr[] = new int[n];
		    String inputLine[] = br.readLine().trim().split(" ");
		    
		    //inserting elements in the array
		    for(int i=0; i<n; i++){
		        arr[i] = Integer.parseInt(inputLine[i]);
		    }
		    
		    Solution obj = new Solution();
		    
		    StringBuffer str = new StringBuffer();
		    ArrayList<Integer> res = new ArrayList<Integer>();
		  
		    //calling leaders() function
		    res = obj.leaders(arr, n);
		    
		    //appending result to a String
		    for(int i=0; i<res.size(); i++){
		        str.append(res.get(i)+" ");
		    }
		    
		    //printing the String
		    System.out.println(str);
		}
		
	}
}

// } Driver Code Ends


class Solution{
    //Function to find the leaders in the array.
    static ArrayList<Integer> leaders(int arr[], int N){
        ArrayList<Integer> list = new ArrayList<>();
        
        if (N==1){
            list.add(arr[0]);
            return list;
        }
        
        list.add(arr[N-1]);
        int max=arr[N-1],currMax= arr[N-1];
        for(int i=N-2;i>=0;i--){
            currMax = Math.max(currMax,arr[i]);
            // max = Math.max(currMax,max);
            if (max<currMax || currMax==arr[i]) {
                max = currMax;
                list.add(max);
            }
        }
        Collections.reverse(list);
        return list;
        
        
    }
}
