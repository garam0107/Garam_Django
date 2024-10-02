from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# django는 User 모델을 직접 참조하는 것을 권장하지 않는다?
# why? User 클래스의 이름이 바뀌거나 다른 user class로 대체 되는 상황이 오면 User를 참조한 부분을 다 바꿔야 하기 때문에
# 유지보수가 힘들어 진다
# User 모델을 간접적으로 참조할 수 있는 방법을 별도로 제공.
# from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserchangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name','last_name', 'email' )


