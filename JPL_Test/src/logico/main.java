package logico;
import java.lang.Integer;
import java.util.Map;
import java.util.Scanner;

import org.jpl7.*;

public class main {

	public static void main(String[] args) {
		//Query q1 = new Query("consult", new Term[] {new Atom("C:\\Users\\Aquiles\\Documents\\Prolog\\Aquiles_arbol.pl")});
		Query q1 = new Query("consult", new Term[] {new Atom("C:\\Users\\jmlma\\Google Drive\\Semestre 15\\Programacion Logica\\3. Practicas\\Compendio I\\Aquiles_arbol.pl")});
		q1.hasSolution();
		int consulta = 0;      
		
		System.out.println("Bienvenidos a Java con Prolog.");
		do {
			consulta = pedirConsulta();
		}while(consulta != -1);
			
		System.exit(0);
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

	public static int pedirConsulta() {
		System.out.println("");
		System.out.println("1-> Verificar parientes de una persona.");
		System.out.println("2-> Verificar relacion entre 2 personas.");
		System.out.println("3-> Salir.");
		Scanner scanner= new Scanner(System.in); 
		String consultaSrt = scanner.nextLine();
		Integer opc = Integer.parseInt(consultaSrt);
		if (opc == 1){
			verificarParientes();
			return 1;
		}else if (opc == 2){
			verificarParentezco();
			return 1;
		}else {
			return -1;
		}
	}

	public static void verificarParientes(){
		System.out.println("Elija una de las siguientes relaciones: ");
		System.out.println("Seleccione una relacion\n\n1- Hermanos\n2- Abuelo\n3- Tio\n4- Primo\n5- Pareja\n6- Suegro\n7- Cunado\n\n");
		Scanner scanner= new Scanner(System.in);
		String relacionSrt = scanner.nextLine();
		Integer relacion = Integer.parseInt(relacionSrt);

		switch (relacion){
			case 1:
				realizarConsultaPariente("hermano");
				break;
			case 2:
				realizarConsultaPariente("abuelo");
				break;
			case 3:
				realizarConsultaPariente("tio");
				break;
			case 4:
				realizarConsultaPariente("primo");
				break;
			case 5:
				realizarConsultaPariente("pareja");
				break;
			case 6:
				realizarConsultaPariente("suegro");
				break;
			case 7:
				realizarConsultaPariente("cunado");
				break;
			default:
				realizarConsultaPariente("_");
				break;
		}
	}

	private static void realizarConsultaPariente(String relacion) {
		//Query checkWorkspace = new Query("consult", new Term[] {new Atom("C:\\Users\\Aquiles\\Documents\\Prolog\\Aquiles_arbol.pl")});
		Query checkWorkspace = new Query("consult", new Term[] {new Atom("C:\\Users\\jmlma\\Google Drive\\Semestre 15\\Programacion Logica\\3. Practicas\\Compendio I\\Aquiles_arbol.pl")});
		checkWorkspace.hasSolution();
		System.out.println("Especifique la persona");
		Scanner scanner= new Scanner(System.in);
		String persona = scanner.nextLine();
		String next = "";
		//loop que itera para todas las soluciones
		try {
			Query query = new Query(relacion+"("+ "X" + "," + persona + ").");
			while (query.hasNext()) {
				Map<String, Term> binding = query.next();
				Term x = (Term) binding.get("X");
				Term y = (Term) binding.get("Y");
				System.out.println(x +" es " + relacion + " de " + persona);
			}
		}
		catch(Exception e) {
			System.out.println("Error en la consulta intente de nuevo.");
		}
	}
	
	private static void verificarParentezco() {
		/*Método para opción 2 del menú*/
	}
}