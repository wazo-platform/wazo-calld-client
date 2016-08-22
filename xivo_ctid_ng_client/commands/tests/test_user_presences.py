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

from xivo_lib_rest_client.tests.command import RESTCommandTestCase

from ..user_presences import UserPresencesCommand


class TestUserPresences(RESTCommandTestCase):

    Command = UserPresencesCommand

    def test_get_presence(self):
        user_uuid = 'user-uuid'

        self.session.get.return_value = self.new_response(200, dict())

        self.command.get_presence(user_uuid)

        self.session.get.assert_called_once_with(
            self.client.url('users', user_uuid, 'presences'),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})

    def test_get_presence_from_user(self):
        self.session.get.return_value = self.new_response(200, dict())

        self.command.get_presence_from_user()

        self.session.get.assert_called_once_with(
            self.client.url('users', 'me', 'presences'),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})

    def test_update_presence(self):
        user_uuid = 'user-uuid'

        self.session.put.return_value = self.new_response(204)

        self.command.update_presence(user_uuid, 'available')

        expected_body = {
            'presence': 'available',
        }
        self.session.put.assert_called_once_with(
            self.client.url('users', user_uuid, 'presences'),
            json=expected_body,
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})

    def test_update_presence_from_user(self):
        self.session.put.return_value = self.new_response(204)

        self.command.update_presence_from_user('available')

        expected_body = {
            'presence': 'available',
        }
        self.session.put.assert_called_once_with(
            self.client.url('users', 'me', 'presences'),
            json=expected_body,
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})
