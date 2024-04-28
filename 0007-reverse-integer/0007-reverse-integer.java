class Solution {
    public int reverse(int x) {
        boolean flag = false;
        if (x<0){
            x = Math.abs(x);
            flag = true;
        }

        String str = new StringBuilder(Integer.toString(x)).reverse().toString();
        int reverse = 0;
        try{
            reverse = Integer.parseInt(str);
        }catch(Exception e){
            // do nothing;
        }
        if (flag == true) return (-1)*reverse;
        return reverse;
    }
}