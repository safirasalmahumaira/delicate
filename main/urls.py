from django.urls import path
from . import views
from main.views import show_main, create_item_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_item
from main.views import delete_item
from main.views import add_item_entry_ajax

app_name = 'main'  # Gunakan namespace 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('sale/', views.sale_page, name='sale_page'),  # Route untuk halaman Sale
    path('skincare/', views.skincare_page, name='skincare_page'),  # Route untuk Skincare
    path('makeup/', views.makeup_page, name='makeup_page'),   
    path('create-item-entry/', create_item_entry, name='create_item_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:item_id>/', show_xml_by_id, name='show_xml_by_id'),  # Changed 'id' to 'item_id'
    path('json/<str:item_id>/', show_json_by_id, name='show_json_by_id'),  # Changed 'id' to 'item_id'
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-mood/<uuid:id>', edit_item, name='edit_item'),
    path('delete/<uuid:id>', delete_item, name='delete_item'),
    path('create-mood-entry-ajax', add_item_entry_ajax, name='add_item_entry_ajax'),
]