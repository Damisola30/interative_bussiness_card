from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'card/buss_RF.html')


# def download_business_card(request):
#     template_file = 'card/buss_RF.html'
#     element_id = 'business-card'
#     download_path = 'downloaded_business_card.png'
#     capture_and_download_element(template_file, element_id, download_path)
#     return JsonResponse({'message': 'File downloaded successfully'})
    