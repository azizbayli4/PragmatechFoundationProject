let btn = document.createElement("button");
btn.innerHTML = "Click Me";
document.querySelector(".box").appendChild(btn);

// btn.addEventListener("click", function () {
//   document.querySelector(".box").style.backgroundColor = "Red";
// });

btn.setAttribute("onclick", "myFunction()");
function myFunction() {
  document.querySelector(".box").style.backgroundColor = "Blue";
}
