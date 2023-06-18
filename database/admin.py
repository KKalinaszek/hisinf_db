from django.contrib import admin
from database.models import Board, Section, Question, Answer, Mp3File, Prize, Player, Event
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import json

# Board
class BoardResources(resources.ModelResource):
    class Meta:
        model = Board
        fields = ('id', 'no', 'page', 'title')

class BoardAdmin(ImportExportModelAdmin):
    resource_class = BoardResources

admin.site.register(Board, BoardAdmin)

# Section
class SectionResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        # Retrieve the Board based on "no" and "page" values
        no = row.get('no')
        page = row.get('page')
        try:
            board = Board.objects.get(no=no, page=page)
            # Assign the retrieved Board's ID to the row's board_id field
            row['board_id'] = board.id
        except Board.DoesNotExist:
            # Handle the case when the Board is not found
            row['board_id'] = None

    class Meta:
        model = Section

class SectionAdmin(ImportExportModelAdmin):
    resource_class = SectionResource

admin.site.register(Section, SectionAdmin)

# Question
class QuestionResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        # Retrieve the Board based on "no" and "page" values
        no = row.get('no')
        page = row.get('page')
        try:
            board = Board.objects.get(no=no, page=page)
            # Assign the retrieved Boards's ID to the row's section_id field
            row['board_id'] = board.id
        except Section.DoesNotExist:
            # Handle the case when the Section is not found
            row['section_id'] = None

    class Meta:
        model = Question


# Answer
class AnswerResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        # Retrieve the Question based on "question" value
        question_text = row.get('question')
        try:
            question = Question.objects.get(question=question_text)
            # Assign the retrieved Question's ID to the row's question_id field
            row['question_id'] = question.id
        except Question.DoesNotExist:
            # Handle the case when the Question is not found
            row['question_id'] = None

    class Meta:
        model = Answer

class AnswerAdmin(ImportExportModelAdmin):
    resource_class = AnswerResource

admin.site.register(Answer, AnswerAdmin)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)

# Mp3File
class Mp3FileResource(resources.ModelResource):
    class Meta:
        model = Mp3File
        fields = ('id', 'board', 'file')

class Mp3FileAdmin(ImportExportModelAdmin):
    resource_class = Mp3FileResource

admin.site.register(Mp3File, Mp3FileAdmin)


# Player
class PlayerResource(resources.ModelResource):
    class Meta:
        model = Player
        fields = ('id', 'username', 'points')

class PlayerAdmin(ImportExportModelAdmin):
    resource_class = PlayerResource

admin.site.register(Player, PlayerAdmin)

# Prize
class PrizeResource(resources.ModelResource):
    class Meta:
        model = Prize
        fields = ('id', 'name', 'description', 'points')

class PrizeAdmin(ImportExportModelAdmin):
    resource_class = PrizeResource

admin.site.register(Prize, PrizeAdmin)

# Event
class EventResource(resources.ModelResource):
    class Meta:
        model = Event
        fields = ('id', 'name', 'prizes')

class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource

admin.site.register(Event, EventAdmin)

