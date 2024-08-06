const fs = require("fs");

const input =
    process.platform === "linux"
        ? fs.readFileSync("/dev/stdin").toString().split("\n")
        : fs.readFileSync("example.txt").toString().split("\r\n");


const [n,m] = input[0].split(' ').map((e)=> parseInt(e))

let answer = ''
let result = []
let visited = Array(n+1).fill(0)
const dfs = (x) => {

    if (x == m) {
        answer += result.join(" ")
        answer += '\n'
        // console.log(result.join(" "))
        return
    }

    for (let i=1; i< n+1; i++) {
        if (visited[i] == 0) {
            result.push(i)
            visited[i] = 1
            dfs(x+1)
            visited[i] = 0
            result.pop()
        }
        
    }
}

dfs(0)

console.log(answer)