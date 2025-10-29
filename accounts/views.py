from django.http import JsonResponse
import base64, json
from django.shortcuts import render

def debug_claims(request):
    raw = request.META.get('X-MS-CLIENT-PRINCIPAL')
    if raw:
        decoded = base64.b64decode(raw).decode('utf-8')
        return JsonResponse(json.loads(decoded), safe=False)
    return JsonResponse({'error': 'No principal found'})

def profile_list(request):
    return render(request, 'accounts/profile_list.html')




