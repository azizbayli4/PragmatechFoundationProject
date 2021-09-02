//ededler=[12,45,23,67,89,1,17,90]
let nums = [12, 15, 23, 67, 89, 1152, 17, 90];

//1.Ededler massivində 3-ə bölünüb 5-ə bölünməyən ədədləri ekrana çap edin

for (let i = 0; i < nums.length; i++) {
  if (nums[i] % 3 == 0 && nums[i] % 5 !== 0) {
    console.log(nums[i] + " in position: " + i);
  }
}

console.log("------------------------");

//2.Rəqəmlərinin cəmi 6 dan böyük olan ədədləri göstərin

for (let i = 0; i < nums.length; i++) {
  let x = parseInt(nums[i] / 10);
  let y = nums[i] % 10;
  if (x >= 10) {
    x = parseInt(x / 10);
    x += x;
  }
  if (x + y > 6) {
    console.log(nums[i] + " in position:" + i);
  }
}

console.log("------------------------");

//3.Massivin cut yerdə duran elementlərinin cəmini tapın

for (let i = 0; i < nums.length; i++) {
  if (i % 2 == 0 && i !== 0) {
    console.log(nums[i] + " in position:" + i);
  }
}

console.log("------------------------");

//4.Son rəqəmi 7 olan ədədləri tapın

for (let i = 0; i < nums.length; i++) {
  let x = nums[i] % 10;
  if (x == 7) {
    console.log(nums[i] + " in position:" + i);
  }
}
