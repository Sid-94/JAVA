package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tentativas = 3;
        System.out.println("Digite a Senha, você tem " + (tentativas) + " tentativas!");
        String senha = sc.next();
        int contador = 1;
        while (!senha.equals("TokioPorto") && contador <= 2) {
            System.out.println("Senha Incorreta, tente novamente. \nTentativas Restantes : "+(3-contador));
            contador++;
            senha = sc.next();
        }
        if (senha.equals("TokioPorto")) {
            System.out.println("ACESSO PERMITIDO!");
        } else {
            System.out.println("Acesso Bloqueado! Senha Incorreta!");
        }
        sc.close();
    }
}
