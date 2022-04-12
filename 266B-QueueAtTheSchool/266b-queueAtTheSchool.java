import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n,t;
        String s;
        n = scan.nextInt();
        t = scan.nextInt();
        s = scan.nextLine();
        s = scan.nextLine();
        StringBuilder myStr = new StringBuilder(s);
 
 
        while(t > 0){
	        for(int i = 0; i < n - 1; i++){
	            if(myStr.charAt(i) == 'B' && myStr.charAt(i+1) == 'G'){
	                myStr.setCharAt(i, 'G');
	                myStr.setCharAt(i+1, 'B');
	                if(i != n - 2){
	                    i++;
                    }
                }
            }
	        t--;
        }
        System.out.println(myStr);
 
    }
}
