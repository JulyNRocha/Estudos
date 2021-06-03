const n = 5;
var dia_da_semana;
var err1 = false;

switch (n){
	case 1:
		dia_da_semana = "domingo";
		break;
	case 2:
		dia_da_semana = "segunda";
		break;
	case 3:
		dia_da_semana = "terça";
		break;
	case 4:
		dia_da_semana = "quarta";
		break;	
	case 5:
		dia_da_semana = "quinta";
		break;	
	case 6:
		dia_da_semana = "sexta";
		break;	
	case 7:
		dia_da_semana = "sábado";
		break;
	default:
		var err1= true;
}


if(err1 == false){
	console.log("O dia da semana conrrespondente a "+n+" é "+dia_da_semana);
}else{
	console.log("Esse numero não conrreponde a nenhum dia da semana");
};
