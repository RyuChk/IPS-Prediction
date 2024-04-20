import grpc

def Error(context, statusCode, message):
    context.set_code(statusCode)
    context.set_details(message)
    print(f"code: ${statusCode}, message: ${message}")