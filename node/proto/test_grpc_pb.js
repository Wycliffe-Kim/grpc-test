// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var test_pb = require('./test_pb.js');

function serialize_TestRequest(arg) {
  if (!(arg instanceof test_pb.TestRequest)) {
    throw new Error('Expected argument of type TestRequest');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_TestRequest(buffer_arg) {
  return test_pb.TestRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_TestResponse(arg) {
  if (!(arg instanceof test_pb.TestResponse)) {
    throw new Error('Expected argument of type TestResponse');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_TestResponse(buffer_arg) {
  return test_pb.TestResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var TestServiceService = exports.TestServiceService = {
  request: {
    path: '/TestService/request',
    requestStream: false,
    responseStream: false,
    requestType: test_pb.TestRequest,
    responseType: test_pb.TestResponse,
    requestSerialize: serialize_TestRequest,
    requestDeserialize: deserialize_TestRequest,
    responseSerialize: serialize_TestResponse,
    responseDeserialize: deserialize_TestResponse,
  },
};

exports.TestServiceClient = grpc.makeGenericClientConstructor(TestServiceService);
