var bigsize = "300"; //Размер большой картинки
var smallsize = "150"; //Размер маленькой картинки
function changeSizeImage(im) {
  if(im.height == bigsize) im.height = smallsize;
  else im.height = bigsize;
}