from apps.main.auth_tokens.models import CustomToken


def get_user_by_token(request):
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[
        -1] if 'HTTP_AUTHORIZATION' in request.META else None

    try:
        exam_token = CustomToken.objects.get(key=token)
        if exam_token:
            if exam_token.schedule:
                return exam_token.schedule.student
            else:
                return exam_token.teacher
    except CustomToken.DoesNotExist:
        return False
