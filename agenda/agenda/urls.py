# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from contacts.views import AddContact , ListContact , Home
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
#url(r'^$', home),
url(r'^$', Home.as_view(template_name="home.html"), name="home" ),
url(r'^contact/create$', login_required(AddContact.as_view(template_name="createcontact.html")) , name='createcontact') ,
url(r'^contact/list$', login_required(ListContact.as_view(template_name="allcontacts.html")) , name='allcontact') ,




url(r'^Imagenes/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT, }),

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
