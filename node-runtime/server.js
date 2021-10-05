const grpc = require("grpc");
var protoLoader = require("@grpc/proto-loader");

const PROTO_PATH = "/Users/rahulvramesh/Workspace/grpc_learning_multiple/node-runtime/bidirectional.proto";


const options = {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
  };
  var packageDefinition = protoLoader.loadSync(PROTO_PATH, options);
  const newsProto = grpc.loadPackageDefinition(packageDefinition);
  
  const server = new grpc.Server();
  let news = [
    { message: "hello world" }
  ];
  
  server.addService(newsProto.Bidirectional.service, {
    GetServerResponse: (call) => {
        call.write({ message: news[0].message });
        call.end();
        
    },
  });
  
  server.bindAsync(
    "0.0.0.0:50052",
    grpc.ServerCredentials.createInsecure(),
    (error, port) => {
      console.log("Server running at http://127.0.0.1:50052");
      server.start();
    }
  );