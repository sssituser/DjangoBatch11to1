class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        print()
        self.get_response = get_response
    def __call__(self,request):
        print('Preprocessing of request')
        response = self.get_response(request)
        print('Post processing of request')
        return response
