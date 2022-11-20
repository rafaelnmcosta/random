package musicas;

public class Principal{
	public static void main(String args[]){
		Compositor comp1 = new Compositor("Fael", "Brasil");
		String[] novasMusicas = {"musica1", "musica2", "musica3"};
		comp1.definirMusicas(novasMusicas);

		System.out.println("Compositor cadastrado!\nNumero de compositores: " + Compositor.getTotalCompositores());

		System.out.println("O nome do compositor é " + comp1.getNome());
		comp1.listarMusicas();

		Compositor comp2 = new Compositor("Iury", "Brasil");
		String[] novasMusicas1 = {"musica4", "musica5", "musica6", "musica7", "musica8"};
		comp2.definirMusicas(novasMusicas1);
		
		System.out.println("Compositor cadastrado!\nNumero de compositores: " + Compositor.getTotalCompositores());

		System.out.println("O nome do compositor é " + comp2.getNome());
		comp2.listarMusicas();
	}
}
