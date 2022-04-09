package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        System.out.println("Digite o Primeiro Valor:");
            double A = leitor.nextDouble();
        System.out.println("Digite o Segundo Valor:");
            double B = leitor.nextDouble();
        System.out.println("Digite o Tereciro Valor:");
            double C = leitor.nextDouble();
            double media;
            media = ((A + B + C)/3);

        System.out.println("A média é " + media);
    }
}
