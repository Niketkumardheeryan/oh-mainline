# -*- coding: utf-8 -*-
from __future__ import absolute_import
# vim: set ai et ts=4 sw=4:

# This file is part of OpenHatch.
# Copyright (C) 2014 Elana Hashman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import mysite.bugsets.models

from django.conf import settings


class InlineEditPermissions(object):

    @classmethod
    def can_edit(cls, adaptor_field):
        if settings.DEBUG:
            return True  # All users can edit

        # Only allow django-inplaceedit to edit AnnotatedBug objects
        if isinstance(adaptor_field.obj, mysite.bugsets.models.AnnotatedBug):
            return True

        return False
