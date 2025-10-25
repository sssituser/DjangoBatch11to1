from django.http import HttpResponse
# class MiddleWareExceptionHandling:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         response = self.get_response(request)
#         return response
#     def process_exception(self,request,exception):
#         return HttpResponse(f"<h1> Currently we are facing some technical problem and the error is {exception} and the class name is : {exception.__class__.__name__}</h1>")
class FirstMiddleWare:
    def __init__(self,get_response):
        self.get_response=get_response
   
    def __call__(self,request):
        print("This line printed by middlerware -1 Before processing the request ")
        response = self.get_response(request)
        print("This line printed by middlerware -1 After processing the request ")
        return response
    
class SecondMiddleWare:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("This line printed by middlerware -2 Before processing the request ")
        response = self.get_response(request)
        print("This line printed by middlerware -2 After processing the request ")
        return response