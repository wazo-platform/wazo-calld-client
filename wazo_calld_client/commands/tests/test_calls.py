# Copyright 2015-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that
from hamcrest import equal_to
from wazo_lib_rest_client.tests.command import RESTCommandTestCase

from ..calls import CallsCommand


class TestCalls(RESTCommandTestCase):

    Command = CallsCommand

    def test_list_calls(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list_calls('my-app', 'my-app-instance')

        self.session.get.assert_called_once_with(
            self.base_url,
            headers={'Accept': 'application/json'},
            params={'application': 'my-app', 'application_instance': 'my-app-instance'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_list_calls_from_user(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list_calls_from_user('my-app', 'my-app-instance')

        self.session.get.assert_called_once_with(
            self.client.url('users', 'me', 'calls'),
            headers={'Accept': 'application/json'},
            params={'application': 'my-app', 'application_instance': 'my-app-instance'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_call(self):
        call_id = 'call-id'
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_call(call_id)

        self.session.get.assert_called_once_with(
            self.client.url('calls', call_id),
            headers={'Accept': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_make_call(self):
        self.session.post.return_value = self.new_response(
            201, json={'return': 'value'}
        )

        result = self.command.make_call('my-call')

        self.session.post.assert_called_once_with(
            self.base_url,
            json='my-call',
            headers={'Accept': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_make_call_from_user(self):
        self.session.post.return_value = self.new_response(
            201, json={'return': 'value'}
        )

        result = self.command.make_call_from_user(
            '1234',
            variables={'key': 'value'},
            line_id=43,
            from_mobile=True,
            all_lines=True,
            auto_answer_caller=True,
        )

        expected_body = {
            'extension': '1234',
            'variables': {'key': 'value'},
            'line_id': 43,
            'from_mobile': True,
            'all_lines': True,
            'auto_answer_caller': True,
        }
        self.session.post.assert_called_once_with(
            self.client.url('users', 'me', 'calls'),
            json=expected_body,
            headers={'Accept': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_hangup(self):
        call_id = 'call-id'
        self.session.delete.return_value = self.new_response(
            200, json={'return': 'value'}
        )

        self.command.hangup(call_id)

        self.session.delete.assert_called_once_with(
            self.client.url('calls', call_id),
            headers={'Accept': 'application/json'},
        )

    def test_hangup_from_user(self):
        call_id = 'call-id'
        self.session.delete.return_value = self.new_response(204)

        self.command.hangup_from_user(call_id)

        expected_url = self.client.url('users', 'me', 'calls', call_id)
        self.session.delete.assert_called_once_with(
            expected_url,
            headers={'Accept': 'application/json'},
        )

    def test_connect_user(self):
        call_id = 'call-id'
        user_id = 'user-id'
        self.session.put.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.connect_user(call_id, user_id)

        self.session.put.assert_called_once_with(
            self.client.url('calls', call_id, 'user', user_id),
            headers={'Accept': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_send_dtmf_digits(self):
        call_id = 'call-id'
        self.session.put.return_value = self.new_response(204)
        self.command.send_dtmf_digits(call_id, '1234')
        expected_url = self.client.url('calls', call_id, 'dtmf')
        self.session.put.assert_called_once_with(
            expected_url,
            headers={'Accept': 'application/json'},
            params={'digits': '1234'},
        )

    def test_send_dtmf_digits_from_user(self):
        call_id = 'call-id'
        self.session.put.return_value = self.new_response(204)
        self.command.send_dtmf_digits_from_user(call_id, '1234')
        expected_url = self.client.url('users', 'me', 'calls', call_id, 'dtmf')
        self.session.put.assert_called_once_with(
            expected_url,
            headers={'Accept': 'application/json'},
            params={'digits': '1234'},
        )

    def test_hold_call(self):
        call_id = 'call-id'
        self.session.put.return_value = self.new_response(204)
        self.command.start_hold(call_id)
        expected_url = self.client.url('calls', call_id, 'hold', 'start')
        self.session.put.assert_called_once_with(
            expected_url,
            headers={'Accept': 'application/json'},
        )

    def test_unhold_call(self):
        call_id = 'call-id'
        self.session.put.return_value = self.new_response(204)
        self.command.stop_hold(call_id)
        expected_url = self.client.url('calls', call_id, 'hold', 'stop')
        self.session.put.assert_called_once_with(
            expected_url,
            headers={'Accept': 'application/json'},
        )

    def test_hold_call_from_user(self):
        call_id = 'call-id'
        self.session.put.return_value = self.new_response(204)
        self.command.start_hold_from_user(call_id)
        expected_url = self.client.url('users', 'me', 'calls', call_id, 'hold', 'start')
        self.session.put.assert_called_once_with(
            expected_url,
            headers={'Accept': 'application/json'},
        )

    def test_unhold_call_from_user(self):
        call_id = 'call-id'
        self.session.put.return_value = self.new_response(204)
        self.command.stop_hold_from_user(call_id)
        expected_url = self.client.url('users', 'me', 'calls', call_id, 'hold', 'stop')
        self.session.put.assert_called_once_with(
            expected_url,
            headers={'Accept': 'application/json'},
        )

    def test_answer_call(self):
        call_id = 'call-id'
        self.session.put.return_value = self.new_response(204)
        self.command.answer(call_id)
        expected_url = self.client.url('calls', call_id, 'answer')
        self.session.put.assert_called_once_with(
            expected_url,
            headers={'Accept': 'application/json'},
        )

    def test_answer_call_from_user(self):
        call_id = 'call-id'
        self.session.put.return_value = self.new_response(204)
        self.command.answer_from_user(call_id)
        expected_url = self.client.url('users', 'me', 'calls', call_id, 'answer')
        self.session.put.assert_called_once_with(
            expected_url,
            headers={'Accept': 'application/json'},
        )
