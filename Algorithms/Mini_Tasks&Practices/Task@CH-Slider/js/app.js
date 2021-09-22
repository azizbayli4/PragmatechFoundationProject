let slider = document.querySelector(".slider");
//let slideSayi=3
let box = document.querySelector(".box");
let allBoxesCount = document.querySelectorAll(".box").length;
let boxWidth = box.clientWidth;

slider.style.width = `${allBoxesCount * boxWidth + 50}px`;
let a = intParse(slider - frame.style.width);

leftPos = 0;
function slideLeft() {
  slider.style.left = `${leftPos}px`;
  leftPos += 400;
}

function slideRight() {
  slider.style.left = `${leftPos}px`;
  leftPos -= 400;
  if (allBoxesCount * 400 > a) {
    leftPos = 0;
  }
}
