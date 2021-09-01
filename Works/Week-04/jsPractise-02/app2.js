let a = 0;

function Increase() {
  console.log(a);
  a++;
  if (a <= 10) {
    Increase();
  }
}
Increase();
