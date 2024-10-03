package atelier2;
import java.time.*;

public class Employe extends Personne {
	//Attributs ou variables d'instances
	protected double salaire;
	protected LocalDate dateEmbauche;

	//Constructeur
	protected Employe(String nom, int age, double salaire, LocalDate dateEmbauche ) {
		super(nom,age);
		this.salaire = salaire;
		this.dateEmbauche = dateEmbauche;
	}
	
	public static Employe createEmploye(String nom, int age, double salaire, LocalDate dateEmbauche) {
		if (age < 16 || age > 65) {
			return null;
		}
		else if (dateEmbauche.isAfter(LocalDate.now())) {
			return null;
		}
		else if (salaire < 0 ) {
			return null; 
		}
		else {
			return new Employe(nom,age,salaire,dateEmbauche);
		}
	}
	public double getSalaire() {
		return this.salaire;
	}
	
	public void augmenterLeSalaire(double pourcentage) {
		this.salaire *= (1 + pourcentage);
	}
	
	public int calculAnnuite(){
		 LocalDate aujourdhui = LocalDate.now();
	        
	        
	      long joursEcoules = Duration.between(dateEmbauche.atStartOfDay(), aujourdhui.atStartOfDay()).toDays();
	        
	        
	      return (int) (joursEcoules / 365) + 1;
	}
	
}

