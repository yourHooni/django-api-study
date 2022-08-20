import json
from datetime import datetime

import pytest_django

from rest_framework import status
from rest_framework.reverse import reverse

from user.models import User

USER_FIELDS_COUNT = 5  # serializer user fields count


def test_user_list(rf, client):
    """
        Test user list
    """
    url = reverse(viewname='user')

    # create data for test
    User.objects.create(
        email='admin@test.com',
        name='admin'
    )
    response = client.get(url)

    # assert: if case is not True, raise AssertError
    assert response.status_code == status.HTTP_200_OK
    data = json.loads(response.content)
    assert len(data[0]) == USER_FIELDS_COUNT
