import fs from 'fs';
import _ from 'lodash';

const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const address = 'localhost:7070';
const callbacks = {
  cameraCallback,
  scenarioCallback,
  eventCallback,
  objectCallback,
  testCallback
}

function packageDefinition(protoFile: string) {
  return protoLoader.loadSync(
    protoFile,
    {
      keepCase: true,
      longs: String,
      enums: String,
      defaults: true,
      oneofs: true,
    }
  );
}

function proto(type: string) {
  return grpc.loadPackageDefinition(packageDefinition(`../proto/${type}.proto`));
}

function service(type: string) {
  const _proto = proto(type);
  const _headCharacter = type.at(0)!;
  const _protoName = type.replace(_headCharacter, _headCharacter.toUpperCase());
  return {
    name: type,
    handle: new _proto[`${_protoName}Service`](address, grpc.credentials.createInsecure())
  }
}

function cameraCallback(service: any) {
  service.get_cameras({id: 0}, (error: any, response: any) => {
    errorCallback(error);

    if (response) {
      _(response.data).forEach(camera => {
        service.get_camera({id: camera.id}, (error2: any, response2: any) => {
          errorCallback(error2);
          
          console.log(response2);
        });
      });
    }
  });
}

function scenarioCallback(service: any) {
  service.get_scenarios({id: 0}, (error: any, response: any) => {
    errorCallback(error);

    if (response) {
      _(response.data).forEach(scenario => {
        service.get_scenario({id: scenario.id}, (error2: any, response2: any) => {
          errorCallback(error2);

          console.log(response2);
        });
      });
    }
  });
}

function eventCallback(service: any) {
  const _streaming_event = service.streaming_event({});
  _streaming_event.on('data', (response: any) => {
    console.log(response);
  });
  _streaming_event.on('end', (response: any) => {
    console.log(response);
  });
}

function objectCallback(service: any) {
  const _streaming_object = service.streaming_object({});
  _streaming_object.on('data', (response: any) => {
    console.log(response);
  });
  _streaming_object.on('end', (response: any) => {
    console.log(response);
  });
}

function testCallback(service: any) {
  function log(response: any) {
    console.log(`id: ${response.id}, name: ${response.name}, message: ${response.message}`);
    if (response.li) {
      console.log(response.li);
    }
  }

  function requestCallback(error: any, response: any) {
    errorCallback(error);

    if (response) {
      log(response);
    }
  }
  
  // service.request({ id: 1, name: 'Wycliffe Kim' }, requestCallback);

  // const call = service.request_stream({ id: 2, name: "Won Dong Kim" });
  // call.on('data', (response: any) => {
  //   log(response);
  // });

  // service.request({ id: 1, name: 'Wycliffe Kim' }, requestCallback);
}

function errorCallback(error: any) {
  if (error) {
    console.error('error', error);
  }
}

function main() {
  fs.readdirSync('../proto')
    .map(protoFile => protoFile.replace('.proto', ''))
    .filter(protoName => protoName !== 'scenario')
    .map(protoName => service(protoName))
    .forEach(_service => {
      (callbacks as any)[`${_service.name}Callback`](_service.handle);
    });
}

main();