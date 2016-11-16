# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
# Copyright (C) 2016 Proformatique, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from xivo_lib_rest_client.tests.command import RESTCommandTestCase

from mock import sentinel as s

from ..line_presences import LinePresencesCommand


class TestLinePresences(RESTCommandTestCase):

    Command = LinePresencesCommand

    def test_get_presence(self):
        line_id = 1

        self.session.get.return_value = self.new_response(200, dict())

        self.command.get_presence(line_id)

        self.session.get.assert_called_once_with(
            self.client.url('lines', line_id, 'presences'),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})

    def test_get_presence_with_xivo_uuid(self):
        self.session.get.return_value = self.new_response(200, dict())

        self.command.get_presence(s.line_id, s.xivo_uuid)

        self.session.get.assert_called_once_with(
            self.client.url('lines', s.line_id, 'presences'),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'},
            params={'xivo_uuid': s.xivo_uuid}
        )

    def test_get_presence_with_xivo_uuid_set_to_none(self):
        self.session.get.return_value = self.new_response(200, dict())

        self.command.get_presence(s.line_id, None)

        self.session.get.assert_called_once_with(
            self.client.url('lines', s.line_id, 'presences'),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'},
        )
