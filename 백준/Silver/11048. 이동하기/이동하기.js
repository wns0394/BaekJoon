const fs = require("fs");

const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("example.txt").toString().split("\r\n");

const [num, ...a] = input
const [n, m] = num.split(" ").map((v) => parseInt(v));

let arr = a.map((v) => v.split(" ").map((e) => parseInt(e)))

for (let i=0; i<n; i++) {
  for (let j =0; j<m; j++) {
    if (i == 0 && j >0 ) {
      arr[i][j] += arr[i][j-1]
    } else if ( i >0 && j ==0) {
      arr[i][j] += arr[i-1][j]
    } else if ( i>0 && j >0) {
      arr[i][j] += Math.max(arr[i-1][j],arr[i][j-1],arr[i-1][j-1])
    }
  }
}

console.log(arr[n-1][m-1])