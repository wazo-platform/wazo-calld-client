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

from ..transfers import TransfersCommand


class TestTransfers(RESTCommandTestCase):

    Command = TransfersCommand

    def test_get_transfer(self):
        transfer_id = 'transfer-id'
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_transfer(transfer_id)

        self.session.get.assert_called_once_with(
            '{base}/{transfer_id}'.format(base=self.base_url, transfer_id=transfer_id),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_make_transfer(self):
        self.session.post.return_value = self.new_response(201, json={'return': 'value'})

        result = self.command.make_transfer('transferred', 'initiator', 'context', 'exten', 'blind', {'key': 'value'})

        expected_body = {
            'transferred_call': 'transferred',
            'initiator_call': 'initiator',
            'context': 'context',
            'exten': 'exten',
            'flow': 'blind',
            'variables': {'key': 'value'},
        }
        self.session.post.assert_called_once_with(
            self.base_url,
            json=expected_body,
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_cancel_transfer(self):
        transfer_id = 'transfer-id'

        self.command.cancel_transfer(transfer_id)

        self.session.delete.assert_called_once_with(
            '{base}/{transfer_id}'.format(base=self.base_url, transfer_id=transfer_id),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})

    def test_complete_transfer(self):
        transfer_id = 'transfer-id'

        self.command.complete_transfer(transfer_id)

        self.session.put.assert_called_once_with(
            '{base}/{transfer_id}/complete'.format(base=self.base_url, transfer_id=transfer_id),
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})
