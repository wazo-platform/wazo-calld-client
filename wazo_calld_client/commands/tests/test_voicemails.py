# -*- coding: utf-8 -*-
# Copyright 2016-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that
from hamcrest import equal_to
from mock import ANY
from xivo_lib_rest_client.tests.command import RESTCommandTestCase

from ..voicemails import VoicemailsCommand


class TestTransfers(RESTCommandTestCase):

    Command = VoicemailsCommand

    def test_get_voicemail(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail(42)

        self.session.get.assert_called_once_with(
            '{url}/42'.format(url=self.base_url),
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_voicemail_from_user(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail_from_user()

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_voicemail_folder(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail_folder(42, 1)

        self.session.get.assert_called_once_with(
            '{url}/42/folders/1'.format(url=self.base_url),
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_voicemail_folder_from_user(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail_folder_from_user(1)

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_voicemail_message(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail_message(42, '123')

        self.session.get.assert_called_once_with(
            '{url}/42/messages/123'.format(url=self.base_url),
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_voicemail_message_from_user(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_voicemail_message_from_user('123')

        self.session.get.assert_called_once_with(
            ANY,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_delete_voicemail_message(self):
        self.command.delete_voicemail_message(42, '123')

        self.session.delete.assert_called_once_with(
            '{url}/42/messages/123'.format(url=self.base_url)
        )

    def test_delete_voicemail_message_from_user(self):
        self.command.delete_voicemail_message_from_user('123')

        self.session.delete.assert_called_once_with(ANY)

    def test_move_voicemail_message(self):
        self.session.put.return_value = self.new_response(204)

        self.command.move_voicemail_message(42, '123', 1337)

        self.session.put.assert_called_once_with(
            '{url}/42/messages/123'.format(url=self.base_url),
            json={'folder_id': 1337},
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        )

    def test_move_voicemail_message_from_user(self):
        self.session.put.return_value = self.new_response(204)

        self.command.move_voicemail_message_from_user('123', 1337)

        self.session.put.assert_called_once_with(
            ANY,
            json={'folder_id': 1337},
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        )

    def test_get_voicemail_recording(self):
        self.session.get.return_value = self.new_response(200, body='blob')

        result = self.command.get_voicemail_recording(42, '123')

        self.session.get.assert_called_once_with(
            '{url}/42/messages/123/recording'.format(url=self.base_url),
            headers={'Accept': 'audio/wav'},
        )
        assert_that(result, equal_to('blob'))

    def test_get_voicemail_recording_from_user(self):
        self.session.get.return_value = self.new_response(200, body='blob')

        result = self.command.get_voicemail_recording_from_user('123')

        self.session.get.assert_called_once_with(ANY, headers={'Accept': 'audio/wav'})
        assert_that(result, equal_to('blob'))
