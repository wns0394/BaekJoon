const fs = require("fs");

const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("example.txt").toString().split("\r\n");

const [n,m] = input[0].split(" ").map((v)=>parseInt(v));

let arr = new Array();

for (let i=0; i< n; i++) {
  const ar = input[i+1].split(" ").map((v)=> parseInt(v));
  arr.push(ar)
}


for (let k=0; k < n; k++) {
  for (let i =0; i <n; i++) {
    for (let j = 0; j < n; j++) {
      arr[i][j] = Math.min(arr[i][j], arr[i][k] + arr[k][j])
    }
  }
}

for (let i = 0; i <m; i++) {
  const [a,b,c] = input[i+1+n].split(" ").map((v)=>parseInt(v))
  if (arr[a-1][b-1] <= c) {
    console.log('Enjoy other party')
  } else {
    console.log('Stay here')
  }
}