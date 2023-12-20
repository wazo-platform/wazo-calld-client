#!/usr/bin/env python3
# Copyright 2015-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import find_packages, setup

setup(
    name='wazo_calld_client',
    version='0.1',
    description='a simple client library for the wazo-calld HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_calld_client.commands': [
            'adhoc_conferences = wazo_calld_client.commands.adhoc_conferences:AdhocConferencesCommand',
            'applications = wazo_calld_client.commands.applications:ApplicationsCommand',
            'calls = wazo_calld_client.commands.calls:CallsCommand',
            'conferences = wazo_calld_client.commands.conferences:ConferencesCommand',
            'config = wazo_calld_client.commands.config:ConfigCommand',
            'faxes = wazo_calld_client.commands.faxes:FaxesCommand',
            'lines = wazo_calld_client.commands.lines:LinesCommand',
            'meetings = wazo_calld_client.commands.meetings:MeetingsCommand',
            'relocates = wazo_calld_client.commands.relocates:RelocatesCommand',
            'status = wazo_calld_client.commands.status:StatusCommand',
            'switchboards = wazo_calld_client.commands.switchboards:SwitchboardsCommand',
            'transfers = wazo_calld_client.commands.transfers:TransfersCommand',
            'trunks = wazo_calld_client.commands.trunks:TrunksCommand',
            'voicemails = wazo_calld_client.commands.voicemails:VoicemailsCommand',
        ]
    },
)
