# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
# Copyright (C) 2016 Proformatique, Inc.
#
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import RESTCommand


class LinePresencesCommand(RESTCommand):

    resource = 'presences'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get_presence(self, line_id, xivo_uuid=None):
        kwargs = {'headers': self.headers}
        if xivo_uuid:
            params = {'xivo_uuid': xivo_uuid}
            kwargs['params'] = params

        r = self.session.get(self._client.url('lines', line_id, self.resource), **kwargs)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
