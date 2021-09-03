let x = 1;
let gWeight = 0.065;
let total = 1;

for (let i = 1; i < 64; i++) {
  x = x * 2;
  total += x;
}

console.log(`Total grain amount is : ${total} `);
let totalgWeight = total * gWeight;
console.log(`Total amount (kg) is : ${totalgWeight / 1000} kg`);
console.log(`Total amount (tonne) is : ${totalgWeight / 1000000} metric tons`);
