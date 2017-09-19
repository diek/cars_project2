from django.contrib.auth.models import User
# def add_variable_to_context(request):
#     user = request.user.username
#     return {

#         'testme': user
#     }


def set_base(request):
    current_user = request.user

    if User.objects.filter(pk=current_user.id, groups__name='driver').exists():
        base_html = 'base_driver.html'
    else:
        base_html = 'base.html'

    return {

        'base_html': base_html
    }
