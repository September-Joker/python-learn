from django.urls import path, re_path, register_converter
from . import views, converters

# 在converter文件中完成
register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index),

    # 带变量的URL
    # path('<int:year>', views.year),  # 只接受整数，其他返回404
    path('<int:year>/<str:name>', views.name),


    # 正则匹配
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),


    # 自定义过滤器
    # path('<myint:year>', views.year),
    path('<yyyy:year>', views.year),
]
