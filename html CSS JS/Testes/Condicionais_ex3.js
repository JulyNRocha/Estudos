const n = 3;
const peso = 68;


var err1 = false
switch(n){
	case 1:
		p = peso*0.37;
		plan = "Mercúrio";
		break;
	case 2:
		p = peso*0.88;
		plan = "Vênus";
		break;
	case 3:
		p = peso*0.38;
		plan = "Marte";
		break;
	case 4:
		p = peso*2.64;
		plan = "Júpiter"
		break;
	case 5:
		p = peso*1.15;
		plan = "Saturno"
		break;
	case 6:
		p = peso*1.17;
		plan = "Urano"
		break;
	default:
		var err1 = true;
		break;
}
if (err1 == false){
	console.log("Seu peso em "+plan+" é "+p+" Kgs");
}else{
	console.log("Planeta não encontrado");
}
