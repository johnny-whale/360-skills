from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .models import Result, Category, Department, Assessment, Skill, Employee, Article

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = Employee
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    author = EmployeeSerializer()
    class Meta:
        model = Article
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Skill
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    assessment = AssessmentSerializer()
    evaluator = EmployeeSerializer()
    evaluatee = EmployeeSerializer()
    skill = SkillSerializer()
    class Meta:
        model = Result
        fields = '__all__'

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

router = routers.DefaultRouter()

router.register(r'departments', DepartmentsViewSet)
router.register(r'employees', EmployeesViewSet)
router.register(r'articles', ArticlesViewSet)
router.register(r'results', ResultsViewSet)

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls))
]