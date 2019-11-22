from django.contrib import admin
from .models import Board



@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('board_id', 'board_title', 'board_det', 'board_type', 'board_writer_id', 'board_srv_id', 'board_com_id')
    list_filter = ('board_id', 'board_title', 'board_det', 'board_type', 'board_writer_id')
    list_display_links = ['board_id', 'board_title', 'board_det', 'board_type', 'board_writer_id', 'board_srv_id', 'board_com_id']

