package com.company;

import java.util.Scanner;

public class AreaQuadrado {
    public static void main(String[] args) {
        Scanner lado = new Scanner(System.in);
        System.out.println("Digite o valor do lado do quadrado em cm:");
        double area = lado.nextDouble();
        System.out.println("A área do quadrado de lado " + area + " é " + area*area + " cm^2");
    }
}
