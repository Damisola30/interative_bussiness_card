import os
from django.shortcuts import render
from dotenv import find_dotenv, load_dotenv


# Create your views here.
dotenv_path = find_dotenv()
load_dotenv (dotenv_path)
TEST = os.getenv("EST_ENV_VAR")
print(TEST)
def home(request):
    return render(request, 'card/buss_RF.html')


# def download_business_card(request):
#     template_file = 'card/buss_RF.html'
#     element_id = 'business-card'
#     download_path = 'downloaded_business_card.png'
#     capture_and_download_element(template_file, element_id, download_path)
#     return JsonResponse({'message': 'File downloaded successfully'})
    