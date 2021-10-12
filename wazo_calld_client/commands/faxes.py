# -*- coding: utf-8 -*-
# Copyright 2019-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import CalldCommand


class FaxesCommand(CalldCommand):

    resource = 'faxes'

    def send(self, fax_content, context, extension, caller_id=None):
        url = self._client.url(self.resource)
        headers = self.get_headers()
        headers['Content-Type'] = 'application/pdf'
        fax_infos = {'context': context, 'extension': extension}
        if caller_id:
            fax_infos['caller_id'] = caller_id
        r = self.session.post(url, headers=headers, params=fax_infos, data=fax_content)
        if r.status_code != 201:
            self.raise_from_response(r)
        return r.json()

    def send_from_user(self, fax_content, extension, caller_id=None):
        url = self._client.url('users', 'me', self.resource)
        headers = self.get_headers()
        headers['Content-Type'] = 'application/pdf'
        fax_infos = {'extension': extension}
        if caller_id:
            fax_infos['caller_id'] = caller_id
        r = self.session.post(url, headers=headers, params=fax_infos, data=fax_content)
        if r.status_code != 201:
            self.raise_from_response(r)
        return r.json()
