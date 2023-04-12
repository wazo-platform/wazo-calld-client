# Copyright 2021-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from wazo_calld_client.command import CalldCommand


class ConfigCommand(CalldCommand):
    resource = 'config'

    def get(self):
        headers = self._get_headers()
        url = self.base_url
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def patch(self, config_patch):
        headers = self._get_headers()
        url = self.base_url
        r = self.session.patch(url, headers=headers, json=config_patch)
        self.raise_from_response(r)
        return r.json()
