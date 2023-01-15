import graphene
from graphene_django import DjangoObjectType
from .models import Quizzes, Category, Question, Answer
from graphene_file_upload.scalars import Upload

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "image")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "title", "quiz", "technique", "title", "difficulty")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")


class Query(graphene.ObjectType):
    get_questions = graphene.List(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())
    all_categories = graphene.List(CategoryType)
    all_quizzes = graphene.List(QuizzesType)
    all_questions = graphene.List(QuestionType)
    def resolve_get_questions(root, info, id):
        return Question.objects.filter(quiz=id)
    def resolve_all_quizzes(root, info):
        return Quizzes.objects.all()
    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_questions(root, info):
        return Question.objects.all()

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)



class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        file = Upload(required=True)

    success = graphene.Boolean()
    category = graphene.Field(CategoryType)
    @staticmethod
    def mutate(self, info, name, file, **kwargs):
        category = Category(name=name, image=file)
        category.save()
        return CategoryMutation(success=True)

class QuestionMutation(graphene.Mutation):
    class Arguments:
        quiz_id = graphene.ID(required=True)
        technique = graphene.Int(required=True)
        title = graphene.String(required=True)
        difficulty = graphene.Int(required=True)

    question = graphene.Field(QuestionType)

    @classmethod
    def mutate(cls, root, info, title, technique, difficulty, quiz_id):
        question = Question.objects.create(quiz=Quizzes.objects.get(pk=quiz_id), technique=technique, title=title, difficulty=difficulty)
        question.save()
        return QuestionMutation(question=question)
class QuizzesMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)

    quizzes = graphene.Field(QuizzesType)

    @classmethod
    def mutate(cls, root, info, title, id):
        quizzes = Quizzes.objects.create(category=Category.objects.get(pk=id), title=title)
        quizzes.save()
        return QuizzesMutation(quizzes=quizzes)



class Mutation(graphene.ObjectType):
    create_category = CategoryMutation.Field()
    create_quizzes = QuizzesMutation.Field()
    create_question = QuestionMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
