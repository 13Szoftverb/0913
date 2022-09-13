import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        /*
        * Ma javaból igazából azokat gyakoroltuk amit eddig, random, scanner, if, meg ilyenek.
        *  Össze raktuk a dolgozat feladatot, szóval azzak kell majd sokat törődni
        * Mindennek ellenére, ez is ki lesz kommentelve
        */

        //kör

        Scanner bemenet = new Scanner(System.in); //scanner syntax
        System.out.print("kérek egy számot a kör sugarához");//sima print println helyett nem csinál új sort
        int r = bemenet.nextInt();

        if (r != 0) {//a sugár nem lehet nulla, és ezt így tudjuk vizsgálni
            if (r > 0){//ez arra van, ha a felhasználó negatívat ír be.
                double kor_ker = 2*r*Math.PI;
                double kor_ter = Math.pow(r, 2)*Math.PI;

                System.out.println("kör \nk = "+kor_ker+"\nt = "+kor_ter);
            }else{//A math.abs() tétel lehet akár r*-1
                System.out.println("Ennek az abszolút értékét veszem!");
                r = Math.abs(r);
            }


        }else{
            System.out.println("nem tudok nullával dolgozni!!\n futtass újra!");
        }


        //négyzet, téglalap.
        //ide nem fogom beleírni a nulla és negatív teszteket, mert ott van egyel feljebb.

        System.out.print("A oldal : ");
        int a = bemenet.nextInt();
        System.out.print("b oldal : ");
        int b = bemenet.nextInt();

        if (a != b){//tesztelünk, hogy az eltének e az oldalak hossza,
                    // mert attól függ hogy ez mi, négyzet, vagy téglalap
            System.out.println("Ez egy téglalap!");
            double tter = a*b;
            double tker = 2*(a+b);
            System.out.println("kerület = "+tker+"\nterület = "+tter);
        }else {
            System.out.println("Ez egy négyzet");
            double nter = Math.pow(a, 2);
            double nker = 4*a;
            System.out.println("kerület = "+nker+"\nterület = "+nter);
        }
        /*az ifeket igazából bármilyen sorrendben, és orientációban lehet csinálni, nekem ez jolt a kézrefekvő*/
    }
}