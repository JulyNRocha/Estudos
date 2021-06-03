const A = 7;
const B = 45;
const C = 27;

if(A>B && A>C){
	if(B>C){
		console.log(A+">"+B+">"+C)
	}else{
		console.log(A+">"+C+">"+B)
	}
}else if(B>A && B>C){
	if(A>C){
		console.log(B+">"+A+">"+C)
	}else{
		console.log(B+">"+C+">"+A)
	}
}else{
	if(A>B){
		console.log(C+">"+A+">"+B)
	}else{
		console.log(C+">"+B+">"+A)
	}
}

