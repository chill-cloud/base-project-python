import 'package:grpc/grpc.dart';

Future<void> main(List<String> args) async {
  final server = Server(
    [
      // You are likely going to bind your server implementation here
      // ServiceNameService(),
    ],
    const <Interceptor>[],
    CodecRegistry(codecs: const [GzipCodec(), IdentityCodec()]),
  );
  await server.serve(port: 9756);
}
