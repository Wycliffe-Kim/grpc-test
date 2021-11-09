import grpc from 'grpc';
import { TestServiceClient } from './proto/test_grpc_pb';
import { TestRequest } from './proto/test_pb';

function main() {
  const address = 'localhost:7070';
  const client = new TestServiceClient(address, grpc.credentials.createInsecure());
  const request = new TestRequest();
  request.setId(1);
  request.setName('Wycliffe Kim');
  console.log(`----- grpc client start ${address} -----`);
  client.request(request, (error, response) => {
    console.log('error', error);
    console.log('response', response);
  });
}

main();