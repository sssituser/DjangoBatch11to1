from django.http import HttpResponse
# class ExecutionFlowMiddleware(object):
#     def __init__(self,get_response):
#         print("Init Method Called")
#         self.get_response = get_response


#     def __call__(self,request):
#         print("preprocessing request")
#         response=self.get_response(request)
#         print("Postprocessing request")
#         return response

class AppMaintainenceMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response



    def __call__(self,request):
        response=self.get_response(request)
        return HttpResponse("<h1>Current Application is Undermaintainence.....</h1>")

        

        
        

        