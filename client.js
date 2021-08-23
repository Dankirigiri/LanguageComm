const net = require("net");
const { stdin, stdout } = require("process");
const { SERVER, PORT, } = require("./config.json")
const readline = require("readline");
const rl = readline.createInterface({input: stdin, output: stdout});
const client = net.createConnection({host:SERVER, port: PORT}, () => {
    console.log("[!] Conectado al server");
});
client.on("data", data => {
    console.log(data.toString);
});
rl.on("line", (input) => {
    client.write(`${input}`);
    if(input == "close"){
        rl.close();
    }
});