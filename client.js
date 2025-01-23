//--------------------------------------------------------------                                       
// the whole section below was copied from the js basics example.                                
//--------------------------------------------------------------

var PROTO_PATH = __dirname + '/correio.proto';

var async = require('async');
var fs = require('fs');
var parseArgs = require('minimist');
var path = require('path');
var _ = require('lodash');
var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
});

var protoDescriptor = grpc.loadPackageDefinition(packageDefinition);


//var correio = grpc.loadPackageDefinition(packageDefinition).correio;
var correio = protoDescriptor.Correio;
//console.log(correio);
var client = new correio('localhost:8080', grpc.credentials.createInsecure());

//--------------------------------------------------------------                                       
// Structure to read from command line
//--------------------------------------------------------------

const readline = require('node:readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

//--------------------------------------------------------------                                       
// Actual code XD
//--------------------------------------------------------------

selectedOption = "";
answered = false;

//client.SendCartas({"texto":"asdasdasd"});
console.log(client.GetCartas({"numero":2}));


// rl.question(
//     "Choose an option: \n 1 = Get all letters \n 2 = Send letter\n",
//     option => {
//         selectedOption = option;
//         rl.close();
//     }
// )

// switch (selectedOption) {
//     case "1":
//         console.log("foda!");
        
//         console.log(client.getCartas());
//         break;

//     case "2":
//         console.log("foda!");
//         rl.question(
//             "Say your message:\n",
//             msg => {
//                 client.sendCartas(msg);
//                 rl.close();
//             }
//         )
//         break;

//     default:
//         break;
// }
