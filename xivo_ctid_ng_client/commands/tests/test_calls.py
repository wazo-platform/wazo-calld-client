# -*- coding: utf-8 -*-

# Copyright (C) 2015-2016 Avencall
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

from hamcrest import assert_that
from hamcrest import equal_to
from xivo_lib_rest_client.tests.command import RESTCommandTestCase

from ..calls import CallsCommand


class TestCalls(RESTCommandTestCase):

    Command = CallsCommand

    def test_list_calls(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list_calls()

        self.session.get.assert_called_once_with(
            self.base_url,
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_list_calls_from_user(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list_calls_from_user('my-app', 'my-app-instance')

        self.session.get.assert_called_once_with(
            self.client.url('users', 'me', 'calls'),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'},
            params={'application': 'my-app',
                    'application_instance': 'my-app-instance'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_call(self):
        call_id = 'call-id'
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_call(call_id)

        self.session.get.assert_called_once_with(
            '{base}/{call_id}'.format(base=self.base_url, call_id=call_id),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_make_call(self):
        self.session.post.return_value = self.new_response(201, json={'return': 'value'})

        result = self.command.make_call('my-call')

        self.session.post.assert_called_once_with(
            self.base_url,
            json='my-call',
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_make_call_from_user(self):
        self.session.post.return_value = self.new_response(201, json={'return': 'value'})

        result = self.command.make_call_from_user('1234', variables={'key': 'value'})

        expected_body = {
            'extension': '1234',
            'variables': {'key': 'value'},
        }
        self.session.post.assert_called_once_with(
            self.client.url('users', 'me', 'calls'),
            json=expected_body,
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_hangup(self):
        call_id = 'call-id'
        self.session.delete.return_value = self.new_response(200, json={'return': 'value'})

        self.command.hangup(call_id)

        self.session.delete.assert_called_once_with(
            '{base}/{call_id}'.format(base=self.base_url, call_id=call_id),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})

    def test_hangup_from_user(self):
        call_id = 'call-id'
        self.session.delete.return_value = self.new_response(204)

        self.command.hangup_from_user(call_id)

        expected_url = self.client.url('users', 'me', 'calls', call_id)
        self.session.delete.assert_called_once_with(expected_url)

    def test_connect_user(self):
        call_id = 'call-id'
        user_id = 'user-id'
        self.session.put.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.connect_user(call_id, user_id)

        self.session.put.assert_called_once_with(
            '{base}/{call_id}/user/{user_id}'.format(base=self.base_url, call_id=call_id, user_id=user_id),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))
