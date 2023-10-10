from django.http import HttpResponse, JsonResponse

def home_page(request):
    friends=[
        'ankit',
        'kartik',
        'gautam'
    ]

    return HttpResponse(friends)