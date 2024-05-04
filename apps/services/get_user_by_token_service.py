from apps.main.auth_tokens.models import CustomToken


def get_student_by_token(request):
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[
        -1] if 'HTTP_AUTHORIZATION' in request.META else None

    try:
        exam_token = CustomToken.objects.get(key=token)
        if exam_token:
            get_user = exam_token.schedule.student
            return get_user
    except CustomToken.DoesNotExist:
        return False
