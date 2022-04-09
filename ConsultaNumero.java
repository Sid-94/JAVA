package com.company;

import java.util.Scanner;

public class ConsultaNumero {
    public static void main(String[] args) {
        Scanner numero = new Scanner(System.in);
        System.out.println("Insira um número que diremos se ele é positivo ou negativo:");
        int consulta = numero.nextInt();

        if (consulta>=0) {
            System.out.println("O número é positivo!");
        } else {
            System.out.println("O númro é negativo!");
        }
    }
}
