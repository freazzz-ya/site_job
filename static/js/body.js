function idd(id) { return document.getElementById(id); }

//Позиция по вертикали
function totop(){ return self.pageYOffset || (document.documentElement && document.documentElement.scrollTop) || (document.body && document.body.scrollTop); }

// Управление мухой
function fly () {

//Определяем высоту и ширину Боди - 100px для полета мухи (чтобы без прокрутки при ее вращении). 
var hei = document.getElementsByTagName("body")[0].offsetHeight-100;
var wi = document.getElementsByTagName("body")[0].offsetWidth-100;

//Вращаем муху случайным образом 
idd("fly").style.transform="rotate("+(Math.random()*360)+"deg)";

//Перемещаем случайным образом
idd("fly").style.top=(Math.random()*hei)+"px";
idd("fly").style.left=(Math.random()*wi)+"px";
}
//Вставьте сюда fly (); для первого случайного полета мухи.

//Функция. При нажатии на муху замедляем ее
function flyclick() { idd('fly').style.transition='99999s'; }

//Отдельное рандомное вращение при загрузке и пока сидит. 
idd("fly").style.transform="rotate("+(Math.random()*360)+"deg)";

setInterval( function() {
//Вставьте сюда fly (); для постоянного случайного полета мухи раз в 60 секунд (можно изменить).
//Можно добавить такие же рандомы для облета мухой нужных точек.
//Например (можно в %):
//idd("fly").style.top="1000px";
//idd("fly").style.left="100px";
idd("fly").style.transform="rotate("+(Math.random()*360)+"deg)"; } , (Math.random()*60000));