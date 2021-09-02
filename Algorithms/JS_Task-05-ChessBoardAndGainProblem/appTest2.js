let x = 1;
let gWeight = 0.024;
let total = x;

for (let i = 1; i < 64; i++) {
  x = x * 2;
  total += x;
}
console.log("Total:" + total);
// let totalgWeight = total * gWeight;
// let kgWeight = totalgWeight / 1000;
// console.log(kgWeight + "kg");
