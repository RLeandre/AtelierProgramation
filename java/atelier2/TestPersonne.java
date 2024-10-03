package atelier2;

public class TestPersonne {
    public static void main(String[] args) {
        // Création de quelques instances de Personne
        Personne p1 = new Personne("Alice", 30);
        Personne p2 = new Personne("Bob", 25);
        Personne p3 = new Personne("Alice", 30);

        // Affichage du nombre d'instances créées
        System.out.println("Nombre de personnes créées : " + Personne.getNbPersonnes());

        // Test de comparaison d'âge
        System.out.println("p1 est plus âgée que p2 : " + p1.plusAgeeQue(p2));
        System.out.println("p2 est plus âgée que p3 : " + Personne.plusAgee(p2, p3));

        // Test de l'égalité
        System.out.println("p1 est égal à p3 : " + p1.equals(p3));
        System.out.println("p1 est égal à p2 : " + p1.equals(p2));
    }
}
