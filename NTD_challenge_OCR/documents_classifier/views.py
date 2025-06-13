from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from documents_classifier.document_processor.processor_pipeline import processor_pipeline


@csrf_exempt
@require_POST
def process_document(request):
    uploaded_file = request.FILES.get("file")
    if not uploaded_file:
        return JsonResponse({"error": "No file provided"}, status=400)

    processed_text_data = processor_pipeline(uploaded_file)
    return JsonResponse(processed_text_data, status=201)
