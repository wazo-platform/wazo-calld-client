# -*- coding: utf-8 -*-
# Copyright (C) 2016 Avencall
# Copyright (C) 2016 Proformatique, Inc.
# SPDX-License-Identifier: GPL-3.0+

from mock import sentinel as s

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

    def test_get_presence_with_xivo_uuid(self):
        self.session.get.return_value = self.new_response(200, dict())

        self.command.get_presence(s.user_uuid, s.xivo_uuid)

        self.session.get.assert_called_once_with(
            self.client.url('users', s.user_uuid, 'presences'),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'},
            params={'xivo_uuid': s.xivo_uuid}
        )

    def test_get_presence_with_xivo_uuid_set_to_none(self):
        self.session.get.return_value = self.new_response(200, dict())

        self.command.get_presence(s.user_uuid, None)

        self.session.get.assert_called_once_with(
            self.client.url('users', s.user_uuid, 'presences'),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'},
        )

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
