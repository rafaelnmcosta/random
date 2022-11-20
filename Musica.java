package musicas;

public class Musica{
	private String titulo;
	private Compositor compositor;

	/*-- Construtor -----------------------*/
	public Musica(String titulo, Compositor compositor){
		this.titulo = titulo;
		this.compositor = compositor;
	}

	/*-- Metodos --------------------------*/
	public void mostrarCompositor(){
		System.out.println("O compositor é: " + this.compositor);
	}
	
	/*-- Getters e Setters ----------------*/
	public String getTitulo(){
		return this.titulo;
	}

	public void setTitulo(String titulo){
		this.titulo= titulo;
	}

	public Compositor getCompositor(){
		return this.compositor;
	}

	public void setCompositor(Compositor compositor){
		this.compositor = compositor;
	}
}

