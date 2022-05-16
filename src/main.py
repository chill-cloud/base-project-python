import grpc
import asyncio

async def serve():
    server = grpc.aio.server()
    # You are likely going to bind your server implementation here
    # api_pb 2_grpc.add_ServiceNameServicer_to_server(ServiceName(), server)
    listen_addr = '[::]:80'
    server.add_insecure_port(listen_addr)
    await server.start()
    try:
        await server.wait_for_termination()
    finally:
        await server.stop(0)

if __name__ == '__main__':
    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        pass
