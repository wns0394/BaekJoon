const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("example.txt").toString().split("\r\n");

// 가장 가까운거 부터하는것은 의미가 없다.
// 완탐 돌려야 할 듯?
// 순열을 구한다.

// 방향을 지정하는 dx, dy
const dx = [0, 1, 0, -1]
const dy = [1, 0, -1, 0]

// js에서 입력값 확인을 위한 index
let index = 0

// 입력이 주어지는동안 돌린다
while (true) {
  // n,m 받아옴
  const [m, n] = input[index].split(" ").map((v) => parseInt(v))

  // n,m이 0이라면 중단
  if (n == 0 && m == 0) {
    break
  }

  // index 증가시켜주고
  // 나머지 입력값들 가져옴
  index += 1

  // 방 정보 arr
  const arr = []

  // 먼지 정보 dirty
  const dirty = []

  // 시작지점 sx,sy
  let sx = 0
  let sy = 0

  for (let i = index; i < index + n; i++) {
    arr.push(input[i].split(""))
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (arr[i][j] == '*') {
        dirty.push([i, j])
      } else if (arr[i][j] == 'o') {
        sx = i
        sy = j
      }
    }
  }

  const bfs = (x, y) => {
    const q = []
    q.push([x, y])
    const visited = Array.from(Array(n), () => Array(m).fill(0))
    visited[x][y] = 1

    while (q.length > 0) {
      const [x, y] = q.shift()

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i]
        const ny = y + dy[i]

        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
          if (arr[nx][ny] == '.' && visited[nx][ny] == 0) {
            q.push([nx, ny])
            visited[nx][ny] = visited[x][y] + 1
          } else if (arr[nx][ny] == '*' && visited[nx][ny] == 0) {
            q.push([nx, ny])
            visited[nx][ny] = visited[x][y] + 1
          } else if (arr[nx][ny] == 'o') {
            q.push([nx, ny])
            visited[nx][ny] = visited[x][y] + 1
          }
        }
      }
    }
    return visited
  }

  // 시작지점에서 모든칸의 이동 거리를 측정한 a
  const a = bfs(sx, sy)

  // 로봇청소기가 모든 먼지에 갈 수 있는지 체크하기 위한 flag
  let flag = true
  
  // 시작점 부터 먼지까지의 거리를 알기 위한 sto
  const sto = []

  // 모든 먼지 좌표에서
  for (let i = 0; i < dirty.length; i++) {
    //  만약 로봇청소기가 먼지에 갈 수 없다면
    if (a[dirty[i][0]][dirty[i][1]] == 0) {
      // 불가능하므로 -1 출력하고 flag는 false
      console.log(-1)
      flag = false
      break
    } else {
      // 그게 아니라면 시작지점부터 먼지까지의 거리 리스트에 넣어주기
      sto.push(a[dirty[i][0]][dirty[i][1]] - 1)
    }
  }
  // n개 만큼의 index 추가해주기
  index += n

  // flag가 false라면 다음 행동은 무의미하다
  if (flag == false) {
    continue
  }

  // 먼지의 개수 k
  const k = dirty.length

  // 각 먼지들 사이의 거리를 저장하기 위한 distance
  distance = Array.from(Array(k), () => Array(k).fill(0))

  // 각 먼지들 사이의 거리 구하기
  for (let i = 0; i < k - 1; i++) {
    // 시작점 dirty[i][0], dirty[i][1]으로 부터의 모든 거리 구하기
    let c = bfs(dirty[i][0], dirty[i][1])
    // 도착점 dirty[j][0], dirty[j][1]까지의 거리 담아주기
    // i가 출발지고 j가 도착지이다
    for (let j = i + 1; j < k; j++) {
      distance[i][j] = c[dirty[j][0]][dirty[j][1]] - 1
      // 출발 도착지가 바뀌어도 거리는 같다
      distance[j][i] = distance[i][j]
    }
  }

  let result = 100000000000000000

  // 모든 경우의 수 순열을 담기위한 p
  let p = []
  let vi = Array(k).fill(0)

  // 순열 permutation 구현
  // 우리는 k개 이므로 0,k-1까지의 index가 필요
  const permutation = (depth, re) => {
    if (depth == k) {
      let count = sto[re[0]]
      for (let i=1; i< k; i++) {
        count += distance[re[i-1]][re[i]]
      }
      result = Math.min(result,count)
      // p.push([...re])
    }

    for (let i = 0; i < k; i++) {
      if (vi[i] == 0) {
        re.push(i)
        vi[i] = 1
        permutation(depth + 1, re)
        vi[i] = 0
        re.pop()
      }
    }
  }

  permutation(0, [])


  // const len_p = p.length

  // for (let i = 0; i < len_p; i++) {
  //   // 각각의 경우마다 거리를 확인하기 위한 count
  //   let count = 0
  //   // 우선 시작지점과 첫번째로 정하는 먼지의 거리를 더해준다
  //   count += sto[p[i][0]]

  //   // 다음 순열부터 앞 뒤 거리를 구해서 count에 더해준다.
  //   for (let j = 0; j < p[i].length - 1; j++) {
  //     count += distance[p[i][j]][p[i][j + 1]]
  //   }

  //   // 최소값으로 갱신
  //   if (count < result) {
  //     result = count
  //   }
  // }
  console.log(result)
}