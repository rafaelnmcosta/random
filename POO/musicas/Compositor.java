package musicas;

public class Compositor{
	private String nome;
	private String pais;
	private Musica[] musicas = new Musica[99];
	static int totalCompositores = 0;

	/*-- Construtor -----------------------*/
	public Compositor(String nome, String pais){
		this.nome = nome;
		this.pais = pais;
		totalCompositores += 1;
	}

	public Compositor(String nome, String pais, Musica[] musicas){
		this.nome = nome;
		this.pais = pais;
		this.musicas = musicas;
		totalCompositores += 1;
	}

	/*-- Metodos --------------------------*/
	public void listarMusicas(){
		System.out.println("Lista de músicas:");
		for(int i=0; i<this.musicas.length; i++){
			if(this.musicas[i] != null){
				System.out.println((i+1) + " - " + this.musicas[i].getTitulo());
			}
			else break;
		}
	}

	public void definirMusicas(String[] tituloDasMusicas){
		int i;
		for (i=0; i<tituloDasMusicas.length; i++){
			Musica novaMusica = new Musica(tituloDasMusicas[i], this);
			musicas[i] = novaMusica;
		}
	}

	/*-- Getters e Setters ----------------*/

	public String getNome(){
		return this.nome;
	}

	public void setNome(String nome){
		this.nome = nome;
	}

	public String getPais(){
		return this.pais;
	}

	public void setPais(String pais){
		this.pais = pais;
	}

	public static int getTotalCompositores(){
		return totalCompositores;
	}

}
