package atelier2;
import java.time.LocalDate;

public class Manager extends Employe {
	private Secretaire secretaire;
	//Constructeur
	protected Manager(String nom, int age, double salaire, LocalDate dateEmbauche) {
        super(nom, age, salaire, dateEmbauche);
    }

    public static Manager createManager(String nom, int age, double salaire, LocalDate dateEmbauche) {
        Employe employe = Employe.createEmploye(nom, age, salaire, dateEmbauche);
        if (employe != null) {
            return new Manager(nom, age, salaire, dateEmbauche);
        }
        return null;
    }


	
	@Override
	public void augmenterLeSalaire(double pourcentage) {
		this.salaire *= (1 + pourcentage/100 + this.calculAnnuite()*0.005);
	}
	
	
	
	public void addSecretaire(Secretaire secretaire) {

	    addSecretaire(secretaire, false);
	}

	public void addSecretaire(Secretaire secretaire, boolean ajout_ext) {

	    if (secretaire.managers.size() <= 5) {
	    
	        this.secretaire = secretaire; 
	        if (!ajout_ext) {
	        	System.out.println("Secretaire  : " + secretaire.getNom()  + " Ajouté pour Manager : " + this.getNom());
	            secretaire.addManager(this,true); 
	        }
	    } else {
	        System.out.println("Cette secrétaire : " + secretaire.getNom() + "a déjà 5 managers et ne peut en avoir davantage.");
	    }
	}

	public void deleteSecretaire(Secretaire secretaire) {
	    deleteSecretaire(secretaire, false);
	}
	
	public void deleteSecretaire(Secretaire secretaire, boolean suppr_ext) {
        if (this.secretaire.equals(secretaire)) {
        
        	if (!suppr_ext) {
        		System.out.println("Secretaire  : " + secretaire.getNom()  + " Supprimé pour Manager : " + this.getNom());
        		this.secretaire.deleteManager(this,true); 
        	}
        		
        		this.secretaire = Secretaire.createSecretaire("Aucune Secretaire", 0, 0, LocalDate.now());
        } else {
        		System.out.println("Cette secretaire : " + secretaire.getNom() + "  n'est pas attribuée à ce Manager : " + this.getNom());
        }
       
        
    }
}
