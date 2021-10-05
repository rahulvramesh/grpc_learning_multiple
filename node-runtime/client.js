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

const NewsService = grpc.loadPackageDefinition(packageDefinition).Bidirectional;

const client = new NewsService(
  "localhost:50052",
  grpc.credentials.createInsecure()
);

console.log("Connection");

// client.GetServerResponse({}, (error, news) => {
//     if (!error) throw error
//       console.log(news);
//   });
let call = client.GetServerResponse();

call.on('data',function(response){
  console.log(response.message);
});

call.on('end',function(){
  console.log('End');
});
