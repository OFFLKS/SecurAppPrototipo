import java.util.ArrayList;
import java.util.Scanner;

public class PetManager {
    private ArrayList<Pet> pets = new ArrayList<>();
    private Scanner scanner = new Scanner(System.in);

    public void cadastrarPet() {
        Pet pet = new Pet();
        System.out.println("Digite o nome do pet: ");
        pet.setNome(scanner.nextLine());

        System.out.println("Digite a espécie do pet: ");
        pet.setEspecie(scanner.nextLine());

        System.out.println("Digite a raça do pet: ");
        pet.setRaca(scanner.nextLine());

        System.out.println("Digite a idade do pet: ");
        pet.setIdade(scanner.nextInt());

        pets.add(pet);
        System.out.println("Pet cadastrado com sucesso!");
    }

    public void listarPets() {
        for (Pet pet : pets) {
            System.out.println("ID: " + pet.getId() + ", Nome: " + pet.getNome() + ", Espécie: " + pet.getEspecie());
        }
    }

    // Métodos de alterar e excluir podem ser adicionados
}
