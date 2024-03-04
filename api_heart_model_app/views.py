from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.conf import settings 
import os 
import joblib

class Prediction_Heart(APIView):
    def post(self,request):
        model_file = os.path.join(settings.BASE_DIR,'api_heart_model_app','best_model_heartdiseases.pkl')
        modelo = joblib.load(model_file)
        data = request.data
        try:
            pred = modelo.predict([[
                data['EDAD'],
                data['SEXO'],
                data['DM2'],
                data['HAS'],
                data['OBESIDAD'],
                data['INFARTO_PREVIO'],
                data['FALLA_RENAL'],
                data['ALCOHOLISMO'],
                data['TABAQUISMO'],
            ]])
            return Response({'Nivel de riesgo':pred[0]},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)