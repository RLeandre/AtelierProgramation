package atelier2;


import java.time.LocalDate;

public class TestEntreprise {
    public static void main(String[] args) {
   
        Employe[] employes = new Employe[8];

     
        employes[0] = Manager.createManager("Alice", 35, 3000, LocalDate.of(2020, 1, 15));
        employes[1] = Manager.createManager("Bob", 40, 3200, LocalDate.of(2019, 5, 20));
        employes[2] = Secretaire.createSecretaire("Claire", 30, 2500, LocalDate.of(2021, 3, 10));
        employes[3] = Secretaire.createSecretaire("David", 28, 2400, LocalDate.of(2022, 7, 5));
        employes[4] = Manager.createManager("Eve", 45, 3500, LocalDate.of(2018, 8, 30));
        employes[5] = Manager.createManager("Tee", 80, 3500, LocalDate.of(2018, 8, 30));
        employes[6] = Manager.createManager("Tee2", 40, -3, LocalDate.of(2018, 8, 30));
        employes[7] = Manager.createManager("Tee3", 40, 10, LocalDate.of(2025, 8, 30));
        

        ((Manager) employes[0]).addSecretaire((Secretaire) employes[2]);  
        ((Manager) employes[1]).addSecretaire((Secretaire) employes[2]);
        
        ((Secretaire) employes[2]).deleteManager((Manager) employes[0]);
        
        ((Secretaire) employes[3]).deleteManager((Manager) employes[0]);
        ((Secretaire) employes[2]).deleteManager((Manager) employes[4]);
        

        ((Secretaire) employes[2]).addManager((Manager) employes[4]);
        ((Secretaire) employes[3]).addManager((Manager) employes[1]);
        
        ((Secretaire) employes[2]).getListeManagers();
        ((Secretaire) employes[3]).getListeManagers();
        
        for (Employe employe : employes) {
        	if (employe != null) {
        		employe.augmenterLeSalaire(10);
        	}
            
        }

        for (Employe employe : employes) {
        	if (employe != null) {
            System.out.println("Nom : " + employe.getNom() + ", Salaire : " + employe.getSalaire());
        	}
        	else {
        		System.out.println("Employe non valide");
        	}
        }
    }
}
