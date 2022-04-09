package com.company;

import java.util.Scanner;

public class VerificaNota {
    public static void main(String[] args) {
        Scanner nota = new Scanner(System.in);
        System.out.println("Entre 0 a 10, qual foi sua nota no período?");
        double periodo = nota.nextDouble();

        if ( periodo == 10) {
            System.out.println("Sua nota é Muito Boa!");
        } if (8<=periodo && periodo<10) {
            System.out.println("Sua nota é Notável!");
        } if (7<=periodo && periodo<8){
            System.out.println("Sua nota é Boa!");
        } if (6<=periodo && periodo<7){
            System.out.println("Sua nota é Suficiente!");
        } if (periodo<6) {
            System.out.println("Sua nota é Insuficiente!");
        } if (10<periodo){
            System.out.println("Sua nota não corresponde a uma nota válida!");
        }
    }
}
