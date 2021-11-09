#!/bin/bash

# # Generate JavaScript code
# yarn run grpc_tools_node_protoc --js_out=import_style=commonjs,binary:./proto --grpc_out=./proto --plugin=protoc-gen-grpc=./node_modules/.bin grpc_tools_node_protoc_plugin -I ../proto ../proto/test.proto

# # Generate TypeScript code (d.ts)
# yarn run grpc_tools_node_protoc --plugin=protoc-gen-ts=./node_modules/.bin/protoc-gen-ts --ts_out=./proto -I ../proto ../proto/test.proto

# generate js codes 
yarn run protoc-gen-grpc --js_out=import_style=commonjs,binary:./proto --grpc_out=./proto --proto_path ../proto ../proto/test.proto
 
# generate d.ts codes 
yarn run protoc-gen-grpc-ts --ts_out=service=true:./proto --proto_path ../proto ../proto/test.proto