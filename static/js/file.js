
function start(){
g=JSON.parse(Save).color
d=document.getElementById('body')
d.style.background==g}

window.onload=sart()

function drop(){
var a=document.getElementById('drop');
if(a.style.display==='none'){
a.style.display='block';
}
else{
a.style.display='none'
}
}

function showform(){
var b=document.getElementById('hidef');
if(b.style.display==='none'){
b.style.display='block';
}
else{
b.style.display='none'
}
}

function showreplyform(a){
var c=document.getElementById(a);
if(c.style.display==='none'){
c.style.display='block';
}
else{
c.style.display='none'
}
}



function sticky(){
var icon=document.getElementById('icon')
var Wheight=window.innerHeight
var Sheight=document.body.scrollHeight
var Spos=window.scrollY
var total=Sheight-Wheight

if(total<=Spos||Spos==0){
icon.style.display='block'
}
else{
icon.style.display='none'
}
}

//window.onscroll=sticky()
window.addEventListener('scroll', sticky)

function edit(){
var form2=document.getElementById('form2')
var bodyp=document.getElementById('bodyprofile')
form2.classList.toggle('form2hide')
bodyp.classList.toggle('bodyprofilehide')

}

function change(g){
var get=document.getElementById(g);
if(get.style.color==='rgb(117, 117, 117)'){
get.style.color='blue';
save=JSON.stringify({'color':'Blue'})
}
else{
get.style.color='#757575'
}
}

function dark(){
    //var chang=document.getElementById('body');
    var chang=document.body;
    k=chang.classList.toggle('Dmode');
   var box=document.getElementById('box');
    //g=box.classList.add('Dmode')
    //c=d.style.background
    //localStorage.setItem(d)
    //Save=JSON.stringify({'color':d})
} 

function filter(){
    var ok=document.getElementById('filter')
    ok.classList.toggle('form2hide')
}