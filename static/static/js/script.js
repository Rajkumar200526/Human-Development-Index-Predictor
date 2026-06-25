// ========================================
// Animated Counter
// ========================================

let count = 0;

let interval = setInterval(function(){

count++;

document.getElementById("countries").innerHTML = count;

if(count==193){

clearInterval(interval);

}

},15);