# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
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

import json

from xivo_lib_rest_client.tests.command import RESTCommandTestCase

from ..chats import ChatsCommand


class TestCalls(RESTCommandTestCase):

    Command = ChatsCommand

    def test_send_message(self):
        self.session.post.return_value = self.new_response(204)

        self.command.send_message('alice-uuid', 'bob-uuid', 'alice', 'hello')

        expected_body = {
            'from': 'alice-uuid',
            'to': 'bob-uuid',
            'alias': 'alice',
            'msg': 'hello',
        }
        self.session.post.assert_called_once_with(
            self.base_url,
            data=json.dumps(expected_body),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})

    def test_send_message_from_user(self):
        self.session.post.return_value = self.new_response(204)

        self.command.send_message_from_user('bob-uuid', 'alice', 'hello')

        expected_body = {
            'to': 'bob-uuid',
            'alias': 'alice',
            'msg': 'hello',
        }
        self.session.post.assert_called_once_with(
            self.base_url,
            data=json.dumps(expected_body),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})
