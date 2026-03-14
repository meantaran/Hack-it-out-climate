let chart

function register(){

fetch("/register",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({

username:document.getElementById("reguser").value,
password:document.getElementById("regpass").value

})

}).then(r=>r.json()).then(data=>alert(data.message))

}


function login(){

fetch("/login",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({

username:document.getElementById("user").value,
password:document.getElementById("pass").value

})

}).then(r=>r.json()).then(data=>{

if(data.status=="success"){

document.getElementById("auth").style.display="none"
document.getElementById("dashboard").style.display="block"

initGlobe()

}else{

alert("Invalid Login")

}

})

}


function initGlobe(){

const globe = Globe()

(document.getElementById('globe'))

.globeImageUrl('//unpkg.com/three-globe/example/img/earth-dark.jpg')

}


function loadClimate(){

let location=document.getElementById("location").value

fetch("/climate",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({location})

})

.then(r=>r.json())

.then(data=>{

let ctx=document.getElementById("chart")

if(chart) chart.destroy()

chart=new Chart(ctx,{

type:"line",

data:{

labels:["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],

datasets:[{

label:"Temperature",

data:data,

borderColor:"cyan",
backgroundColor:"rgba(0,255,255,0.2)"

}]

}

})

})

}


function downloadReport(){

let location=document.getElementById("location").value

fetch("/report",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({location})

})

.then(res=>res.blob())

.then(blob=>{

let url=window.URL.createObjectURL(blob)

let a=document.createElement("a")

a.href=url

a.download="climate_report.pdf"

a.click()

})

}
