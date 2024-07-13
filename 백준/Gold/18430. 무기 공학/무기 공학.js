const fs = require("fs");
const { join } = require("path");
const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("example.txt").toString().split("\r\n");

const [num, ...a] = input
const [n, m] = num.split(" ").map((v) => parseInt(v));

const arr = a.map((v) => v.split(" ").map((e) => parseInt(e)))

let visited = Array.from(Array(n), () => Array(m).fill(0))

const dx = [[1, 0], [1, 0], [-1, 0], [-1, 0]]
const dy = [[0, 1], [0, -1], [0, 1], [0, -1]]

let result = 0

const dfs = (x, y, count) => {
  result = Math.max(result, count)

  if (x == n) {
    return;
  }
  if (visited[x][y] == 0) {
    for (let i = 0; i < 4; i++) {
      const [x1, y1] = [x + dx[i][0], y + dy[i][0]]
      const [x2, y2] = [x + dx[i][1], y + dy[i][1]]

      if (0 <= x1 && x1 < n && 0 <= y1 && y1 < m && 0 <= x2 && x2 < n && 0 <= y2 && y2 < m && visited[x1][y1] == 0 && visited[x2][y2] == 0) {
        visited[x1][y1] = 1
        visited[x2][y2] = 1
        visited[x][y] = 1

        if (y == m - 1) {
          dfs(x + 1, 0, count + arr[x][y] * 2 + arr[x1][y1] + arr[x2][y2])
        } else {
          dfs(x, y + 1, count + arr[x][y] * 2 + arr[x1][y1] + arr[x2][y2])
        }
        visited[x1][y1] = 0
        visited[x2][y2] = 0
        visited[x][y] = 0

      }
    }

  }
  if (y == m - 1) {
    dfs(x + 1, 0, count)
  } else {
    dfs(x, y + 1, count)
  }
}

dfs(0, 0, 0)

console.log(result)