const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("example.txt").toString().split("\r\n");

const [n, m] = input[0].split(" ").map((v) => parseInt(v));

const bisectLeft = (arr,value) => {
  let left = 0;
  let right = n;

  while ( left < right ) {
    const mid = Math.floor((left+right)/2);
    if (arr[mid] < value) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
}

const bisectRight = (arr,value) => {
  let left = 0;
  let right = n;

  while ( left < right ) {
    const mid = Math.floor((left+right)/2);
    if (arr[mid] <= value) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
}

const arr = input[1].split(" ").map((v) => parseInt(v));


arr.sort((a,b) =>( a - b));

const result = new Array();
for (let i = 2; i < m+2; i++) {
  const [s,e] = input[i].split(" ").map((v) => parseInt(v));
  answer = bisectRight(arr,e) - bisectLeft(arr,s)
  result.push(answer)
}
console.log(result.join('\n'))
