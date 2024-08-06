const fs = require("fs");

const input =
    process.platform === "linux"
        ? fs.readFileSync("/dev/stdin").toString().split("\n")
        : fs.readFileSync("example.txt").toString().split("\r\n");

const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

const [num, ...a] = input;
const [n, m] = num.split(" ").map(Number);
const arr = a.map((e) => e.split(" ").map(Number));

const virus = [];
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        if (arr[i][j] === 2) {
            virus.push([i, j]);
        }
    }
}

const inf = 1e9;
let result = inf;

const bfs = (selectedViruses) => {
    const visited = Array.from(Array(n), () => Array(n).fill(0));
    const q = [];
    
    selectedViruses.forEach(([x, y]) => {
        q.push([x, y, 0]); // (x, y, time)
        visited[x][y] = 1;
    });

    let maxTime = 0;

    while (q.length > 0) {
        const [x, y, time] = q.shift();

        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < n && visited[nx][ny] === 0 && arr[nx][ny] !== 1) {
                visited[nx][ny] = 1;
                q.push([nx, ny, time + 1]);
                if (arr[nx][ny] === 0) {
                    maxTime = time + 1;
                }
            }
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (arr[i][j] === 0 && visited[i][j] === 0) {
                return;
            }
        }
    }
    result = Math.min(result, maxTime);
}

const dfs = (start, count, selectedViruses) => {
    if (count === m) {
        bfs(selectedViruses);
        return;
    }

    for (let i = start; i < virus.length; i++) {
        selectedViruses.push(virus[i]);
        dfs(i + 1, count + 1, selectedViruses);
        selectedViruses.pop();
    }
}

dfs(0, 0, []);

console.log(result === inf ? -1 : result);