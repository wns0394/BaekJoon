const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("example.txt").toString().split("\r\n");


for (let a=0; a < input.length; a++) {

    arr = input[a].split("")
    
    let mo = ['a','i','y', 'e', 'o', 'u']
    let ja = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
    
    let result = ''
    
    for (let i = 0; i < arr.length; i++) {
        if (mo.includes(arr[i].toLowerCase())) {
            if (arr[i] == arr[i].toLowerCase()) {
                result += mo[(mo.indexOf(arr[i].toLowerCase())+3)%6]
            } else {
                result += mo[(mo.indexOf(arr[i].toLowerCase())+3)%6].toUpperCase()
            }
        } else if (ja.includes(arr[i].toLowerCase())) {
            if (arr[i] == arr[i].toLowerCase()) {
                result += ja[(ja.indexOf(arr[i].toLowerCase())+10)%20]
            } else {
                result += ja[(ja.indexOf(arr[i].toLowerCase())+10)%20].toUpperCase()
            }
        } else {
            result += arr[i]
        }
    }
    
    console.log(result)
}