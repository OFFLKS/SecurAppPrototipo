public class PetShopApp {
    public static void main(String[] args) {
        PetManager petManager = new PetManager();
        
        petManager.cadastrarPet();
        petManager.listarPets();
    }
}
