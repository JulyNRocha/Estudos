const Segundos = 8000;

const Horas = Math.round(Segundos/3600);
const Minutos = Math.round((Segundos % 3600)/60);
const RestSegundos = Math.round((Segundos % 3600) % 60);


console.log(Segundos+" segundos também são: "+Horas+":"+Minutos+":"+RestSegundos);
