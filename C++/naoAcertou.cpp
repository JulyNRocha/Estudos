#include <map>
#include <string>

extern std::string palavraSecreta;
extern std::map<char, bool> chutou;

bool naoAcertou(){
	int cont;
	for (char letra : palavraSecreta ){
		if(!chutou[letra]){
			return true;
		}
	}
	return false;
}