from rest_framework import routers

from article.apis import ArticleViewSet
from hackathon.apis import HackViewSet
from project.apis import ProjectViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r"proj", ProjectViewSet, base_name="proj")
router.register(r"article", ArticleViewSet, base_name="article")
router.register(r"hack", HackViewSet, base_name="hack")
