package com.pucmm.arbolgenealogicoprolog;

import org.jpl7.Query;
import org.jpl7.Term;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.Map;
import java.util.Scanner;

@SpringBootApplication
public class ArbolGenealogicoPrologApplication {

    public static void main(String[] args) {
        SpringApplication.run(ArbolGenealogicoPrologApplication.class, args);

        Query q = new Query("consult('resources/arbol.pl')");
        q.hasSolution();

        System.out.println("Elija una opcion\nPersona1:\n\n");

        System.out.println("1- orlando\n2- alfonso\n3- luis\n4- carlos\n5- pedro\n6- maria\n7- karla\n8- lola\n9- julia\n10- Aleatorio\n\n");

        Scanner scanner = new Scanner(System.in);

        String persona1 = scanner.nextLine();

        System.out.println("Seleccione una relacion\n\n1- hermanos\n2- abuelo\n3- tio\n4- primo\n5- pareja\n6- suegro\n7- cunado\n\n");

        String relacion = scanner.nextLine();

        System.out.println("Persona2:\n\n1- orlando\n2- alfonso\n3- luis\n4- carlos\n5- pedro\n6- maria\n7- karla\n8- lola\n9- julia\n10- Aleatorio\n\n");

        String persona2 = scanner.nextLine();

        q = new Query(relacion+"("+persona1+", "+persona2+")");

        Map<String, Term>[] res = q.allSolutions();

        for(int i=0; i < res.length; i++)
        {
            System.out.println(res[i]);
        }
    }

}
