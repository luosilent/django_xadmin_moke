# -*- coding: utf-8 -*-
# __author__ = 'luo'
# __time__ = '2017/9/3 0003 22:53'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDicAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'fav_nums', 'click_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'fav_nums', 'click_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'fav_nums', 'click_nums', 'image', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums',
                   'add_time']


xadmin.site.register(CityDict, CityDicAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)