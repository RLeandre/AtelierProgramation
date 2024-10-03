package atelier2;

import java.time.LocalDate;
import java.util.ArrayList;

public class Secretaire extends Employe {
	protected ArrayList<Manager> managers;
	//Constructeur
	
	protected Secretaire(String nom, int age, double salaire, LocalDate dateEmbauche) {
        super(nom, age, salaire, dateEmbauche);
        this.managers = new ArrayList<>();
    }

    public static Secretaire createSecretaire(String nom, int age, double salaire, LocalDate dateEmbauche) {
        Employe employe = Employe.createEmploye(nom, age, salaire, dateEmbauche);
        if (employe != null) {
            return new Secretaire(nom, age, salaire, dateEmbauche);
        }
        return null;
    }
    public void getListeManagers() {
    	System.out.println("Lite des Managers de : " + this.getNom());
    	for (Manager manager : managers) {
        	System.out.println(manager.getNom());
        }
    }

	
	@Override
	public void augmenterLeSalaire(double pourcentage) {
		this.salaire *= (1 + pourcentage/100 + managers.size()*0.001);
	}
	
	public void addManager(Manager manager) {
	    addManager(manager, false);
	}

	public void addManager(Manager manager, boolean ajout_ext) {
	    if (managers.size() <= 5) {

	        this.managers.add(manager);
	        if (!ajout_ext) {
		    	System.out.println("Manager  : " +  manager.getNom() + " Ajouté pour Secretaire : " + this.getNom());
	            manager.addSecretaire(this,true);
	        }
	    } else {
	        System.out.println("Cette secrétaire : " + this.getNom() + " a déjà 5 managers et ne peut en avoir davantage.");
	    }
	}
	public void deleteManager(Manager manager) {
	    deleteManager(manager, false);
	}
	
	public void deleteManager(Manager manager, boolean suppr_ext) {
		if (managers.contains(manager)) {
			
			this.managers.remove(manager);
			if (!suppr_ext) {
				System.out.println("Manager  : " +  manager.getNom() + " Supprimé pour Secretaire : " + this.getNom());
				manager.deleteSecretaire(this,true); 
			}
			
		}
		else {
			System.out.println("Cette secretaire : " + this.getNom() + " n'as pas ce manager : "+ manager.getNom() + " d'attribué ");
		}
     
        
        
    }


	
}
