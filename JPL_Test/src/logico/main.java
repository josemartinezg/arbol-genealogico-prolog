package logico;
import java.lang.Integer;
import java.util.Map;
import java.util.Scanner;

import org.jpl7.*;

public class main {

	public static void main(String[] args) {
//		Query q1 = new Query("consult", new Term[] {new Atom("C:\\Users\\Aquiles\\Documents\\Prolog\\Aquiles_arbol.pl")});
		Query q1 = new Query("consult", new Term[] {new Atom("C:\\Users\\jmlma\\Google Drive\\Semestre 15\\Programacion Logica\\3. Practicas\\Compendio II\\arbolg.pl")});
	//	System.out.println("consult " + (q1.hasSolution() ? "succeded" : "failed"));
		q1.hasSolution();
		 String consulta = "";      
		
		System.out.println("Bienvenidos a Java con Prolog.");
			do {
				pedirConsulta();
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
		catch(Exception e) {
		   System.out.println("Error en la consulta intente de nuevo.");
		}
	}

	public static void pedirConsulta() {
		System.out.print("1-> Verificar parientes de una persona.");
		System.out.print("2-> Verificar relaci�n entre 2 personas.");
		System.out.print("3-> Salir.");
		Scanner scanner= new Scanner(System.in); 
		String consultaSrt = scanner.nextLine();
		Integer opc = Integer.parseInt(consultaSrt);
		if (opc == 1){
			verificarParientes();
		}else if (opc == 2){
			verificarParentezco();
		}
	}

	private static void verificarParentezco() {
	}

	public static void verificarParientes(){
		System.out.print("Elija una de las siguientes relaciones: ");
		System.out.println("Seleccione una relacion\n\n1- Hermanos\n2- Abuelo\n3- Tio\n4- Primo\n5- Pareja\n6- Suegro\n7- Cunado\n\n");
		Scanner scanner= new Scanner(System.in);
		String relacionSrt = scanner.nextLine();
		Integer relacion = Integer.parseInt(relacionSrt);

		switch (relacion){
			case 1:
				realizarConsultaPariente("hermano");
			case 2:
				realizarConsultaPariente("abuelo");
			case 3:
				realizarConsultaPariente("tio");
			case 4:
				realizarConsultaPariente("primo");
			case 5:
				realizarConsultaPariente("pareja");
			case 6:
				realizarConsultaPariente("suegro");
			case 7:
				realizarConsultaPariente("cuando");
			default:
				realizarConsultaPariente("_");
		}
	}

	private static void realizarConsultaPariente(String relacion) {
//		Query checkWorkspace = new Query("consult", new Term[] {new Atom("C:\\Users\\Aquiles\\Documents\\Prolog\\Aquiles_arbol.pl")});
		Query checkWorkspace = new Query("consult", new Term[] {new Atom("C:\\Users\\jmlma\\Google Drive\\Semestre 15\\Programacion Logica\\3. Practicas\\Compendio II\\arbolg.pl")});
		checkWorkspace.hasSolution();
		System.out.print("Especifíque la persona");
		Scanner scanner= new Scanner(System.in);
		String persona = scanner.nextLine();
		String next = "";
		//loop que itera para todas las soluciones
		try {
			Query query = new Query(relacion+"("+ persona + ", X)");
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
		catch(Exception e) {
			System.out.println("Error en la consulta intente de nuevo.");
		}
	}
}