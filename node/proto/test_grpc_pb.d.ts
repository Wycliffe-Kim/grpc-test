// package: 
// file: test.proto

import * as grpc from 'grpc';
import * as test_pb from './test_pb';

interface ITestServiceService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
  request: Irequest
}

interface Irequest {
  path: string; // "/.TestService/request"
  requestStream: boolean; // false
  responseStream: boolean; // false
  requestType: test_pb.TestRequest;
  responseType: test_pb.TestResponse;
  requestSerialize: (arg: test_pb.TestRequest) => Buffer;
  requestDeserialize: (buffer: Uint8Array) => test_pb.TestRequest;
  responseSerialize: (arg: test_pb.TestResponse) => Buffer;
  responseDeserialize: (buffer: Uint8Array) => test_pb.TestResponse;
}

export interface ITestServiceClient {
  request(request: test_pb.TestRequest, callback: (error: Error | null, response: test_pb.TestResponse) => void): grpc.ClientUnaryCall;
  request(request: test_pb.TestRequest, metadata: grpc.Metadata, callback: (error: Error | null, response: test_pb.TestResponse) => void): grpc.ClientUnaryCall;
}

export const TestServiceService: ITestServiceService;
export class TestServiceClient extends grpc.Client implements ITestServiceClient {
  constructor(address: string, credentials: grpc.ChannelCredentials, options?: object);
  public request(request: test_pb.TestRequest, callback: (error: Error | null, response: test_pb.TestResponse) => void): grpc.ClientUnaryCall;
  public request(request: test_pb.TestRequest, metadata: grpc.Metadata, callback: (error: Error | null, response: test_pb.TestResponse) => void): grpc.ClientUnaryCall;
}

