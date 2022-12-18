class Solution {
    void reverse(int arr[],int start,int end){
        while(start<end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;end--;
        }
    }
    public void rotate(int[] arr, int K) {
        int N = arr.length;
        K%=N;
        reverse(arr,0,N-1);
        reverse(arr,0,K-1);
        reverse(arr,K,N-1);
    }
}