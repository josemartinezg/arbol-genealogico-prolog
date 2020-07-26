package visual;

import org.jpl7.*;

import java.awt.Color;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.JTextPane;
import javax.swing.border.EmptyBorder;

import logico.main;

public class VentanaConsulta extends JFrame {

	private JPanel contentPane;
	private JTextField tfPersona;
	private JTextField txtProlog;
	
	
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					VentanaConsulta frame = new VentanaConsulta();
					frame.setVisible(true);
				//conectar();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}

			private void conectar() {
				Query q1 = new Query("consult", new Term[] {new Atom("C:\\Users\\Aquiles\\Documents\\Prolog\\Aquiles_arbol.pl")});
				
				System.out.println("consult " + (q1.hasSolution() ? "succeded" : "failed"));
				
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public VentanaConsulta() {
		setTitle("Probando JPL");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 346);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		//Iniciando la conexión con PROLOG
		//Query q1 = new Query("consult", new Term[] {new Atom("C:\\Users\\Aquiles\\Documents\\Prolog\\Aquiles_arbol.pl")});
		JLabel lblAbuelos = new JLabel("Persona:");
		lblAbuelos.setBounds(10, 18, 68, 14);
		contentPane.add(lblAbuelos);
		
		tfPersona = new JTextField();
		tfPersona.setBounds(10, 43, 103, 19);
		contentPane.add(tfPersona);
		tfPersona.setColumns(10);
		
		JComboBox comboBox = new JComboBox();
		comboBox.setModel(new DefaultComboBoxModel(new String[] {"Abuelos", "Hermanos", "Pareja", "Tios", "Primos", "Suegro", "Cu\u00F1ado"}));
		comboBox.setBounds(148, 42, 87, 20);
		contentPane.add(comboBox);
		
		JLabel lblNewLabel = new JLabel("Parentezco:");
		lblNewLabel.setBounds(148, 18, 91, 14);
		contentPane.add(lblNewLabel);
		
		
		
		JButton btnConsultar = new JButton("Consultar");
		
		btnConsultar.setBounds(302, 30, 89, 47);
		contentPane.add(btnConsultar);
		
		JLabel lblNewLabel_1 = new JLabel("Consulta directa a prolog");
		lblNewLabel_1.setBounds(10, 99, 163, 14);
		contentPane.add(lblNewLabel_1);
		
		txtProlog = new JTextField();
		txtProlog.setBounds(10, 124, 163, 20);
		contentPane.add(txtProlog);
		txtProlog.setColumns(10);
		
		JButton btnConsultaProlog = new JButton("Consulta Prolog");
		btnConsultaProlog.setForeground(Color.BLACK);
		btnConsultaProlog.setBounds(183, 123, 130, 23);
		contentPane.add(btnConsultaProlog);
		
		JTextPane txtPane = new JTextPane();
		txtPane.setEditable(false);
		txtPane.setBounds(10, 155, 414, 141);
		contentPane.add(txtPane);
		
		btnConsultar.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String respuesta;
				switch(comboBox.getSelectedItem().toString()) {
						
				case "Abuelos":
					//respuesta = main.NewQuery(tfPersona.toString(), comboBox.getSelectedItem().toString());
					//txtPane.setText(respuesta);
					break;
					
				case "Hermanos":
					
					break;
					
				case "Pareja":
					
					break;
					
				case "Tios":
					
					break;
					
				case "Primos":
					
					break;
					
				case "Suegro":
					break;
					
				case "Cu\\u00F1ado":
					break;
				}
			}
		});


		btnConsultaProlog.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				//String respuesta = main.Prolog(txtProlog.toString());
			//	txtPane.setText(respuesta);
				
			}
		});
	
	}
}
