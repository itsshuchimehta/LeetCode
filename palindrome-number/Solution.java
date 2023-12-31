class Solution {
    public boolean isPalindrome(int x) {
        String str = Integer.toString(x);
        String nstr="";
        char ch;
         for(int i=str.length()-1; i>=0; i--){
            ch = str.charAt(i);
            nstr += ch;
	    }
       	return nstr.equals(str);
    }
}
