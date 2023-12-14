from rareapi.models import Rare_User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    rare_user = Rare_User.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if rare_user is not None:
        data = {
            'id': rare_user.id,
            'uid': rare_user.uid,
            'bio': rare_user.bio
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new rare_user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the levelupapi_rare_user table
    rare_user = Rare_User.objects.create(
        bio=request.data['bio'],
        uid=request.data['uid']
    )

    # Return the rare_user info to the client
    data = {
        'id': rare_user.id,
        'uid': rare_user.uid,
        'bio': rare_user.bio
    }
    return Response(data)
