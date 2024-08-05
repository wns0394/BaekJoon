const fs = require("fs");

const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")  
    : fs.readFileSync("example.txt").toString().split("\r\n");


const dx = [-1,0,1,0]
const dy = [0,1,0,-1]

const [num,...a] = input
const [n,m] = num.split(" ").map((e)=> parseInt(e))
const arr = a.map((v) => v.split(" ").map((e) => parseInt(e)))
const visited = Array.from(Array(n), () => Array(m).fill(0))

const q = []

for (let i=0; i<n; i++) {
    for (let j=0; j < m; j++) {
        if (arr[i][j] == 2) {
            q.push([i,j])
            visited[i][j] = 1
        }
    }
}

while (q.length > 0) {
    const [x,y] = q.shift()

    for (let i=0; i < 4; i++) {
        const nx = x + dx[i]
        const ny = y + dy[i]

        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
            if (arr[nx][ny] == 1 && visited[nx][ny] == 0) {
                q.push([nx,ny])
                visited[nx][ny] = visited[x][y] + 1
            }
        }
    }
}

for (let i=0; i<n; i++) {
    let result = []
    for (let j=0; j < m; j++) {
        if (visited[i][j]) {
            result.push(visited[i][j]-1)
        } else {
            if (arr[i][j]) {
                result.push(-1)
            } else {
                result.push(0)
            }
        }
    }
    console.log(result.join(" "))
}