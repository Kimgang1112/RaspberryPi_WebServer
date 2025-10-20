var num=document.getElementById('num');
var transport=document.getElementById('transport');
var increase=document.getElementById('increase');

var number=0;
num.innerHTML=number;

increase.addEventListener("click", function (){

    num.innerHTML=++number;
});

transport.addEventListener("click", async ()=>{
    let res= await fetch("/submit", {
        method:"POST",
        headers:{"Conteㅜt-Type":"application/json"},
        body: JSON.stringify({value:number})
    });

    number=0;
    num.innerHTML=number;

});