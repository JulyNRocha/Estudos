package bytebankcomposto;

public class TesteGetESet {
	public static void main(String[] args) {
		Conta conta = new Conta(12,35);
		conta.setNumero(1337);
		
		System.out.println(conta.getNumero());
	}
}

