package atelier2;

public class Personne {
	//Attributs ou variables d'instances
	private String nom;
	private int age;
	private static int nbPersonnes = 0; 
	//Constructeur
	public Personne(String nom,int age) {
		this.nom=nom;
		this.age=age;
		
		nbPersonnes++;
	}
	public Personne() {
		this("",0);
	}	
	public static int getNbPersonnes() {
		return nbPersonnes;
	}
	public boolean plusAgeeQue(Personne p2) {
		return this.age > p2.age;
	}
	public static boolean plusAgee(Personne p1, Personne p2) {
		return p1.age > p2.age;
	}
	public  void setNom(String nom) {
		this.nom=nom;
	}
	public  void setAge(int age) {
		this.age=age;
	}
	public int getAge() {
		return this.age;
	}
	public String getNom() {
		return this.nom;
	}
	public void afficher() {
		System.out.println("Nom : "+this.nom + "\nAge : " + this.age );
	}
	public String toString() {
		return this.nom + " (" + this.age + " ans)";
	}
	@Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        Personne P2 = (Personne) obj;
        
        return this.nom == P2.nom && this.age == P2.age;
    }

}
