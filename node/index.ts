const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const PROTO_PATH = '../proto/test.proto';

function packageDefinition() {
  return protoLoader.loadSync(
    PROTO_PATH,
    {
      keepCase: true,
      longs: String,
      enums: String,
      defaults: true,
      oneofs: true,
    }
  );
}

function testProto() {
  return grpc.loadPackageDefinition(packageDefinition());
}

function main() {
  const address = 'localhost:7070';
  const testproto = testProto();
  const client = new testproto.TestService(address, grpc.credentials.createInsecure());
  client.request({ id: 1, name: 'Wycliffe Kim' }, (error: any, response: any) => {
    if (error) {
      console.error(error);
    }

    if (response) {
      console.log(`id: ${response.id}, name: ${response.name}, message: ${response.message}`);
    }
  });
}

main();