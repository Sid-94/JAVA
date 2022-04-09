package com.company;

import java.util.Scanner;

public class NumeroPrimo {
    public static void main(String[] args) {
        Scanner numero = new Scanner(System.in);
        System.out.println("Insira um número inteiro para saber se ele é primo ou não:");
        int primo = numero.nextInt();

        int divisor = 0;

        System.out.println("O número " + primo + " possui os seguintes divisores: ");
        for (int contador = 1; contador <= primo; contador++) {

            if (primo % contador == 0) {
                divisor++;
                System.out.print(contador + " ");
            }
        }
        if (divisor == 2){
            System.out.println("\nO número " + primo + " é primo!");
        } else {
            System.out.println("\nO número " + primo + " não é primo!");
        }
    }
}
