from openai import OpenAI
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from google import genai
from google.genai import types
from django.views.decorators.csrf import csrf_exempt


client = genai.Client(api_key=settings.GEMINI_API_KEY)

# client = OpenAI(api_key=settings.OPENAI_API_KEY)

def load_system_prompt():
    with open("prompts/unihelp_template.md", "r", encoding="utf-8") as f:
        return f.read()
    

@csrf_exempt
@api_view(["POST"])
def chat_with_unihelp(request):
    try:
        SYSTEM_TEMPLATE = load_system_prompt()
        user_message = request.data.get("message", "")

        
        config = types.GenerateContentConfig(
            system_instruction=SYSTEM_TEMPLATE, 
            temperature=0.4,
            max_output_tokens=600,
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", 
            contents=user_message,   
            config=config,
        )

        answer = response.text

        return Response({"response": answer})

    except Exception as e:
        return Response(
            {"error": f"An unexpected error occurred. {str(e)}"},
            status=500
        )