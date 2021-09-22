let circle = document.querySelector(".box");
let a = 10;

// window.addEventListener("load", (e) => {
//   circle.style.position = "absolute";
//   circle.style.left = 0;
//   circle.style.top = 0;
// });

window.addEventListener("keydown", (e) => {
  switch (e.key) {
    case "ArrowLeft":
      let x = parseInt(circle.style.left) - a;
      if (x >= 0) {
        circle.style.left = x + "px";
      }
      break;
    case "ArrowRight":
      circle.style.left = `${parseInt(circle.style.left) + a}px`;
      break;
    case "ArrowUp":
      let y = parseInt(circle.style.top) - a;
      if (y >= 0) {
        circle.style.top = y + "px";
      }
      break;
    case "ArrowDown":
      circle.style.top = `${parseInt(circle.style.top) + a}px`;
      break;
    case "ArrowRight" + "ArrowUp":
      circle.style.left = `${parseInt(circle.style.left) + a}px`;
      circle.style.top = `${parseInt(circle.style.top) + a}px`;
      break;
  }
});
