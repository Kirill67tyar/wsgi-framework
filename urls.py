from views import (Index, About, Feedback, )

urlpatterns = {
    '/': Index(),
    '/about/': About(),
    '/feedback/': Feedback(),
}
