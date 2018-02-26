import json

from django.utils.translation import ugettext_lazy as _

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.core.models import EnrollWareGroup, EnrollClassTime, AHACredentials, AHAField, Mapper
from apps.core.tasks import export_to_aha


@api_view(['POST'])
def export_group(request):
    try:
        groups = json.loads(request.data['groups'])
    except:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    tasks = []
    user = request.user

    for group in groups:

        # TODO: add try except, return Error if something not found
        enroll_group = EnrollWareGroup.objects.filter(id=group['enroll_group_id']).first()

        class_time = EnrollClassTime.objects.filter(group_id=enroll_group.group_id).first()

        #TODO: use lookups
        aha_auth_data = AHACredentials.objects.filter(user=user).last()

        group_data = {
            'course': group['aha_data']['course'],
            'language': "English",
            'location': group['aha_data']['location'] + " ",
            'tc': group['aha_data']['tc'],
            'ts': group['aha_data']['ts'],
            'instructor': group['aha_data']['instructor'],
            'date': class_time.date,
            'from': class_time.start,
            'to': class_time.end,
            'class_description': group['aha_data']['class_description'],
            'roster_limit': group['aha_data']['roster_limit'],
            'cutoff_date': group['aha_data']['cutoff_date'],
            'class_notes': group['aha_data']['class_notes']
        }

        # TODO: fix user literal

        MAPPER_FIELDS = (AHAField.FIELD_TYPES.COURSE, AHAField.FIELD_TYPES.LOCATION, AHAField.FIELD_TYPES.INSTRUCTOR)

        # TODO: parallel function
        for field in MAPPER_FIELDS:
            Mapper.objects.update_or_create(
                aha_field=AHAField.objects.filter(type=field).first(),
                enroll_value=getattr(enroll_group, field),
                user=user,
                defaults={'aha_value': group['aha_data'][field]}
            )

        task = export_to_aha.delay(aha_auth_data.username, aha_auth_data.password, group_data)
        tasks.append(task.id)
    return Response({'details':  _("Tasks in progress"), 'tasks': tasks}, status=status.HTTP_200_OK)
