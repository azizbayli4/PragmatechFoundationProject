let accStatus = true;
let allItems = document.querySelectorAll(".acc-item");
function CloseAcc(el) {
  for (let i = 0; i < allItems.length; i++) {
    // allItems[i].querySelector("p").style.display = "none";
    allItems[i].querySelector("p").style.visibility = "hidden";
  }
  if (accStatus == true) {
    // el.nextElementSibling.style.display = "none";
    el.nextElementSibling.style.visibility = "hidden";
    accStatus = false;
  } else {
    // el.nextElementSibling.style.display = "block";
    el.nextElementSibling.style.opacity = "1";
    el.nextElementSibling.style.visibility = "visible";

    accStatus = true;
  }
}
