var icon=document.getElementById('icon')


function sticky(){
var Wheight=window.innerHeight
var Sheight=document.body.scrollHeight
var Spos=window.scrollY
console.log(Spos)
var total=Sheight-Wheight
console.log(total)

if(total<=Spos||Spos==0){
icon.style.display='block'
}
else{
icon.style.display='none'
}
}

window.addEventListener('scroll', sticky)
