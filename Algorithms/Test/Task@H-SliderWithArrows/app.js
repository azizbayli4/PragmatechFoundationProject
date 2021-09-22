function changeImage(elem) {
  // let thumbImage=document.querySelector('.thumb img').getAttribute('src');

  // document.querySelector('.image-frame img').setAttribute('src',thumbImage)

  let thumbImage = elem.querySelector("img").getAttribute("src");
  document.querySelector(".image-frame img").setAttribute("src", thumbImage);
}
