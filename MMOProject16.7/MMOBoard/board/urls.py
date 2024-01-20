from django.urls import path

from board.views import *

urlpatterns = [
    path('board/', PostsListView.as_view(), name='posts_list'),
    path('board/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('board/<int:pk>/post_del_ask/', post_delete_ask, name='post_del_ask'),
    path('board/<int:pk>/post_del_ask/post_del_confirm/', post_delete_confirm, name='post_del_confirm'),
    path('board/<int:pk>/repl_del_ask/<int:repl_pk>/', repl_delete_ask, name='repl_del_ask'),
    path('board/<int:pk>/repl_del_ask/<int:repl_pk>/repl_del_confirm/', repl_delete_confirm, name='repl_del_confirm'),
    path('board/<int:pk>/repl_apr_and_disapr/<int:repl_pk>/', repl_approve_and_disapprove, name='repl_apr_and_disapr'),
    path('board/<int:pk>/repl_rej_and_unrej/<int:repl_pk>/', repl_reject_and_unreject, name='repl_rej_and_unrej'),
    path('posts_search/', PostsSearchView.as_view(), name='posts_search'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('profile_board/<int:pk>/', ProfilePostsView.as_view(), name='profile_posts'),
    path('profile_repls/<int:pk>/', ProfileRepliesView.as_view(), name='profile_repls'),
]
