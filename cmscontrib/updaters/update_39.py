#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contest Management System - http://cms-dev.github.io/
# Copyright © 2018 Stefano Maggiolo <s.maggiolo@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""A class to update a dump created by CMS.

Used by DumpImporter and DumpUpdater.

Add default values (null) to the new admin field in questions, messages and
announcements.

"""


class Updater:

    def __init__(self, data):
        assert data["_version"] == 38
        self.objs = data

    def run(self):
        for k, v in self.objs.items():
            if k.startswith("_"):
                continue
            if v["_class"] == "Question" \
                    or v["_class"] == "Message" \
                    or v["_class"] == "Announcement":
                v["admin"] = None

        return self.objs
