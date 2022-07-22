def generate_response(result=False, code=200, message= "", response = {}):
    response = {
    "result": [
        {
        "encabezado": {
            "result": str(result),
            "StatusCode": str(code),
            "message": str(message)
        },
        "response": response
        }
    ]
    }
    return response

