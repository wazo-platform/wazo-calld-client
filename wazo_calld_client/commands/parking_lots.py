# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from collections.abc import Mapping
from wazo_calld_client.command import CalldCommand


class ParkingLotsCommand(CalldCommand):
    resource = 'parking_lots'

    def get(self, parking_id: int) -> Mapping:
        headers = self._get_headers()
        url = self._client.url(self.resource, parking_id)
        r = self.session.get(url, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
