const A = 8;
const B = 10;
const e = 1;

var err1 = false;

switch(e){
	case 1:
		r = A + B;
		break;
	case 2:
		if(A>B){
			r= A - B;
		}else{
			r= B - A;
		}
		break;
	case 3:
		r = A * B;
		break;
	case 4:
		if(B != 0){
			r = A/B
		}else{
			r = 0;
		}
	default:
		var err1 = true;
		break;
}
if(err1 == false){
	console.log("Seu resultado é:"+e);
}else{
	console.log("Opção invalida");
};


