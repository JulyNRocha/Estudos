#include "ContaCorrente.hpp"


ContaCorrente::ContaCorrente(std::string numero, Titular titular)
	:Conta(numero, titular) {

}

float ContaCorrente::taxaDeSaque() const {
	return 0.05;
};

void ContaCorrente::transferePara(Conta& destino, float valor) {
	saca(valor);
	destino.deposita(valor);
}