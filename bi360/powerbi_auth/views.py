# from django.conf import settings
import requests
from django.http import JsonResponse
from msal import ConfidentialClientApplication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PowerBIAPIView(APIView):

    def get(self, request):
        client = ConfidentialClientApplication(
            "df55816c-6cf0-433c-8cf1-5176eb6585be",
            authority="https://login.microsoftonline.com/63ac2b95-d182-4f73-87fb-b3d60141ca38",
            client_credential="sVu8Q~AxOhARA1BtjwKs5BkTPDVgmafE9~tHTaTH",
        )

        token_response = client.acquire_token_for_client(scopes=[
            "https://graph.microsoft.com/.default",
        ])
        if "access_token" in token_response:
            # Setup the Power BI API URL
            access_token = token_response["access_token"]
            group_id = "118db30a-0311-4a65-8a13-491920317f2a"
            report_id = "b3ec916b-6984-425b-a3b7-fa91a6c15549"
            powerbi_api_url = f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/reports/{report_id}"

            # Make a GET request to the Power BI API
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(powerbi_api_url, headers=headers)

            # If the request is successful, return the embed URL
            print(response)
            if response.status_code == 200:
                embed_url = response.json().get("embedUrl")
                return JsonResponse({"embedUrl": embed_url}, safe=False)
            else:
                return JsonResponse({"error": "Failed to retrieve embed URL"}, status=400)

            return Response({"token": token_response["access_token"]}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Could not acquire token"}, status=status.HTTP_400_BAD_REQUEST)
