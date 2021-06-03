const sexo = "mulher";
const a = 1.62;

if(sexo == "homem"){
	s = 1;
}else if( sexo == "mulher"){
	s = 2;
}else{
	console.log("Genero não encontrado");
}

var err1 = false
switch(s){
	case 1:
		p = (72.7*a) - 58;
		break;
	case 2:
		p = (62.1*a) - 44.7;
		break;

	default:
		var err1 = true;
		break;
}
console.log("Seu peso ideal é "+p+" Kgs");

