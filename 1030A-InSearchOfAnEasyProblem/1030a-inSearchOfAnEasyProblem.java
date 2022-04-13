import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n, a;
        n = scan.nextInt();
        while(n != 0){
            a = scan.nextInt();
            if(a == 1){
                System.out.println("HARD");
                System.exit(0);
            }
            n--;
        }
        System.out.println("EASY");
 
    }
}
