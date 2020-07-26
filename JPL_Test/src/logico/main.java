package logico;
import java.util.Map;
import java.util.Scanner;

import org.jpl7.*;

public class main {

	public static void main(String[] args) {
		Query q1 = new Query("consult", new Term[] {new Atom("C:\\Users\\Aquiles\\Documents\\Prolog\\Aquiles_arbol.pl")});
	//	System.out.println("consult " + (q1.hasSolution() ? "succeded" : "failed"));
		q1.hasSolution();
		 String consulta = "";      
		
		System.out.println("Bienvenidos a Java con Prolog.");
		
		
	
			do {
				consulta = pedirConsulta();
				realizarConsulta(consulta);
				
				}while(consulta != "exit.");
        
     
  	
	

}

	private static void realizarConsulta(String consulta) {
		Scanner scanner= new Scanner(System.in); 
		String next = "";
		
		//loop que itera para todas las soluciones
		try {
		Query query = new Query(consulta);
		while (query.hasNext()) {
		    Map<String, Term> binding = query.next();
		    Term x = (Term) binding.get("X");
		    Term y = (Term) binding.get("Y");
		    if(x != null)
		    System.out.println(x);
		    if(y != null)
		    System.out.println(y);
		    //para delay 
		    next = scanner.nextLine();
		}
		}
	catch(Exception e) 
    { 
       System.out.println("Error en la consulta intente de nuevo.");  
    } 
		
		
	}

	private static String pedirConsulta() {
		System.out.print("Inserte su consulta: ");
		Scanner scanner= new Scanner(System.in); 
		String consulta= scanner.nextLine();  
		return consulta;
	}
}