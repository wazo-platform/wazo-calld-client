# Copyright 2015-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that
from hamcrest import equal_to
from wazo_lib_rest_client.tests.command import RESTCommandTestCase

from ..transfers import TransfersCommand


class TestTransfers(RESTCommandTestCase):
    Command = TransfersCommand

    def test_list_transfers_from_user(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list_transfers_from_user()

        self.session.get.assert_called_once_with(
            self.client.url('users', 'me', 'transfers'),
            headers={'Accept': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_transfer(self):
        transfer_id = 'transfer-id'
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_transfer(transfer_id)

        self.session.get.assert_called_once_with(
            self.client.url('transfers', transfer_id),
            headers={'Accept': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_make_transfer(self):
        self.session.post.return_value = self.new_response(
            201, json={'return': 'value'}
        )

        result = self.command.make_transfer(
            'transferred',
            'initiator',
            'context',
            'exten',
            'blind',
            {'key': 'value'},
            timeout=42,
        )

        expected_body = {
            'transferred_call': 'transferred',
            'initiator_call': 'initiator',
            'context': 'context',
            'exten': 'exten',
            'flow': 'blind',
            'variables': {'key': 'value'},
            'timeout': 42,
        }
        self.session.post.assert_called_once_with(
            self.base_url,
            json=expected_body,
            headers={'Accept': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_make_transfer_from_user(self):
        self.session.post.return_value = self.new_response(
            201, json={'return': 'value'}
        )

        result = self.command.make_transfer_from_user(
            'extension', 'initiator', 'blind', timeout=42
        )

        expected_body = {
            'exten': 'extension',
            'initiator_call': 'initiator',
            'flow': 'blind',
            'timeout': 42,
        }
        self.session.post.assert_called_once_with(
            self.client.url('users', 'me', 'transfers'),
            json=expected_body,
            headers={'Accept': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))

    def test_cancel_transfer(self):
        transfer_id = 'transfer-id'

        self.session.delete.return_value = self.new_response(
            204, json={'return': 'value'}
        )

        self.command.cancel_transfer(transfer_id)

        self.session.delete.assert_called_once_with(
            self.client.url('transfers', transfer_id),
            headers={'Accept': 'application/json'},
        )

    def test_cancel_transfer_from_user(self):
        transfer_id = 'transfer-id'

        self.session.delete.return_value = self.new_response(
            204, json={'return': 'value'}
        )

        self.command.cancel_transfer_from_user(transfer_id)

        self.session.delete.assert_called_once_with(
            self.client.url('users', 'me', 'transfers', transfer_id),
            headers={'Accept': 'application/json'},
        )

    def test_complete_transfer(self):
        transfer_id = 'transfer-id'

        self.session.put.return_value = self.new_response(204, json={'return': 'value'})

        self.command.complete_transfer(transfer_id)

        self.session.put.assert_called_once_with(
            self.client.url('transfers', transfer_id, 'complete'),
            headers={'Accept': 'application/json'},
        )

    def test_complete_transfer_from_user(self):
        transfer_id = 'transfer-id'

        self.session.put.return_value = self.new_response(204, json={'return': 'value'})

        self.command.complete_transfer_from_user(transfer_id)

        self.session.put.assert_called_once_with(
            self.client.url('users', 'me', 'transfers', transfer_id, 'complete'),
            headers={'Accept': 'application/json'},
        )
