# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from contacts.views import home


urlpatterns = patterns('',
    # Examples:
url(r'^$', home),
    # url(r'^blog/', include('blog.urls')),


# url(r'^$', ListPost.as_view(template_name="listpost.html") , name='home'),
# url(r'^detalle/(?P<pk>\d+)$', DetailPost.as_view(template_name="detailpost.html") , name='detalle'),
# url para CRUD para usuarios
# url(r'^post/create$', login_required(PostCreate.as_view(template_name="post_form.html")) , name='createpost')# ,
# url(r'^post/(?P<pk>\d+)/update$', login_required(PostUpdate.as_view(template_name="post_form.html")) , name='updatepost'),
# url(r'^post/(?P<pk>\d+)/delete$', login_required(PostDelete.as_view(template_name="post_form.html")) , name='deletepost'),
# formulario propio
# url(r'^post/(?P<pk>\d+)/add_comment$', login_required(AddComment.as_view(template_name="add_comentario.html")) , name='add_comment'),


url(r'^admin/', include(admin.site.urls)),
)
