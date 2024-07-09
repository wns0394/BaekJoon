const fs = require("fs");
const { join } = require("path");
const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("example.txt").toString().split("\r\n");

const [n,m] = input[0].split(" ").map((v)=> parseInt(v));

let arr = Array.from(Array(n), () => Array(20).fill(0))


for (let i=0; i<m; i++) {
  const [...a] = input[i+1].split(" ").map((v)=> parseInt(v));
  
  if (a[0] == 1) {
    arr[a[1] - 1][a[2] - 1] = 1;
  } else if (a[0] == 2) {
    arr[a[1] - 1][a[2] - 1] = 0;
  } else if (a[0] == 3) {
    arr[a[1] - 1].pop()
    arr[a[1] - 1].unshift(0)
  } else {
    arr[a[1] - 1].shift()
    arr[a[1] - 1].push(0)
  }
}

const check = new Set();

for (let i=0; i<n; i++) {
  check.add(arr[i].join(''))
}
console.log(check.size)