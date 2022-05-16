# Chill example project

Some steps for you to write code with this template:

1. Write your server code in the [`src`](src/) directory;
2. Fill [`api`](api/) directory with gRPC declarations of your API;
3. Use [`protoc`](https://grpc.io/docs/protoc-installation/) to generate stubs by these declarations;
3. Change [Dockerfile in the `image` dir](image/Dockerfile) so that in could run your server;
4. [Follow the docs](https://chill-cloud.github.io/docs/) to manage dependencies for your service, and to deploy it.