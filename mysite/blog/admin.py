from django.contrib import admin
from .models import Post
@admin.register(Post)
#Декоратор

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    #позволяет задавать поля модели, которые вы хотите
    #показывать на странице списка объектов администрирования

    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    #мы определили список полей, по которым можно выполнять поиск

    prepopulated_fields = {'slug': ('title',)}
    #что нужно предзаполнять поле slug данными, вводимыми в поле title, используя атрибут prepopulated_fields

    raw_id_fields = ['author']
    #отображается поисковым виджетом, кото- рый будет более приемлемым, чем выбор из выпадающего списка

    date_hierarchy = 'publish'
    #навигационные ссылки для навигации по иерархии дат

    ordering = ['status', 'publish']
    #были заданы критерии сортировки, которые будут использоваться по умолчанию

