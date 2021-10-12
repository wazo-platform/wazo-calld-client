# Copyright 2019-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_calld_client.command import CalldCommand


class StatusCommand(CalldCommand):

    resource = 'status'

    def get(self):
        headers = self.get_headers()
        url = self.base_url
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()
