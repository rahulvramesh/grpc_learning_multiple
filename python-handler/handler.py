# !env/bin/pyth

"""Handler Function To Get The Request And Connect To Runtime"""

import logging
import bidirectional_client as grpc_client

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 1, Define the JSON Structure to store rutime information
# 2, Generate a request payload

""" Runtimes Information """
runtimes: dict = {
    "python3": "localhost:50051"  # Should Make The Port Constant
}


""" Request Payload , Let's create a global payload structure"""
request_payload: dict = {
    "runtime": "python3",
    "action": "run",
    "payload": "hello",
    "sid": "ABC_788_GHGH"  # For Sandboxing each request
}


def InvokeRuntime(payload: dict) -> bool:
    """
    Invoke the runtime to process the request
    :param payload:
    :return:
    """
    # Find the runtme
    runtime = runtimes[payload["runtime"]]
    logging.info("Invoking Runtime {}".format(runtime))
    grpc_client.run(runtime)

    return False


if __name__ == '__main__':
    print("starting")

    try:
        InvokeRuntime(request_payload)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
