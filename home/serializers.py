from rest_framework import serializers
from .models import Question,Answer
from .custom_relational_fields import EmailNameRelationalFields

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = '__all__'
        # extra_kwargs = {'body': {'read_only': True}}

    User = EmailNameRelationalFields(read_only=True)


      #obj دونه به دونه به آبجکت های سوال ها اشاره دارد
    def get_answers(self, obj):
        answers = obj.whitch_answer.all()
        return AnswerSerializer(instance=answers, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
