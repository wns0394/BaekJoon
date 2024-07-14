const fs = require("fs");

const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("example.txt").toString().split("\r\n");

let [n, k] = input[0].split(" ").map((v) => parseInt(v));

const count = k * (k + 1) / 2
if (count > n) {
  console.log(-1)
} else if ((n-count)% k == 0) {
  console.log(k - 1)
} else {
  console.log(k)
}