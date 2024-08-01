const fs = require("fs");
const input =
    process.platform === "linux"
        ? fs.readFileSync("/dev/stdin").toString().split("\n")
        : fs.readFileSync("example.txt").toString().split("\r\n");

const dx1 = [-1, 0, 1, 0]
const dy1 = [0, 1, 0, -1]
const dx2 = [-1, 0, 1, 0, -1, -1, -2, -2, 1, 1, 2, 2]
const dy2 = [0, 1, 0, -1, -2, 2, -1, 1, 2, -2, 1, -1]


const k = parseInt(input[0])
const [m, n] = input[1].split(" ").map((e) => parseInt(e))

const arr = new Array()

for (let i = 2; i < n + 2; i++) {
    const a = input[i].split(" ").map((e) => parseInt(e));
    arr.push(a)
}

const visited = Array.from(Array(n), () => Array.from(Array(m), () => Array(k + 1).fill(0)))

const q = [];

q.push([0, 0, 0])
visited[0][0][0] = 1

let flag = 1;

while (q.length > 0) {
    const [x, y, z] = q.shift();

    if (x == n - 1 && y == m - 1) {
        flag = 0
        console.log(visited[x][y][z] - 1)
        break
    }

    if (z < k) {
        for (let i = 0; i < 12; i++) {
            let nx = x + dx2[i]
            let ny = y + dy2[i]

            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (arr[nx][ny] == 0) {
                    if (i <= 3 && visited[nx][ny][z] == 0) {
                        q.push([nx, ny, z])
                        visited[nx][ny][z] = visited[x][y][z] + 1
                    } else if (i > 3 && visited[nx][ny][z + 1] == 0) {
                        q.push([nx, ny, z + 1])
                        visited[nx][ny][z + 1] = visited[x][y][z] + 1

                    }
                }
            }
        }
    } else {
        for (let i = 0; i < 4; i++) {
            let nx = x + dx1[i]
            let ny = y + dy1[i]
            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (arr[nx][ny] == 0 && visited[nx][ny][z] == 0) {
                   q.push([nx, ny, z])
                    visited[nx][ny][z] = visited[x][y][z] + 1
                }
            }
        }
    }
}

if (flag) {
    console.log(-1)
}