# wazo-calld-client [![Build Status](https://jenkins.wazo.community/buildStatus/icon?job=wazo-calld-client)](https://jenkins.wazo.community/job/wazo-calld-client)

A python library to connect to wazo-calld. HTTPS is used by default. Certificates are verified by default. To disable certificate verification, use the verify_certificate=False argument when instantiating the client.

Usage:

```python
from wazo_calld_client import Client

c = Client('localhost', token='the-one-ring', verify_certificate='</path/to/trusted/certificate>')

# Get wazo-calld status
status = c.status.get()

optional_args = {
    'application': 'switchboard',
    'application_instance': 'switchboard_blue',
}
calls = c.calls.list_calls(recurse=False, **optional_args)
mycalls = c.calls.list_calls_from_user(**optional_args)  # List calls of the authenticated user

params = {
  "destination": {
    "extension": "8001",
    "context": "default",
    "priority": 1
  },
  "source": {
    "user": "ec008fd8-df3c-427a-8cb7-f94c1d238ad3",
    "line_id": 54,
    "from_mobile": False
  }
}

call = c.calls.make_call(params)
# This does the same thing, but derives the user UUID from the auth token
call = c.calls.make_call_from_user(extension='1234', variables={'key': 'value'}, line_id=54, from_mobile=False)

call
{u'call_id': u'1446422660.20'}


mycall = c.calls.get_call('call_id')

mycall
{
  "status": "Up",
  "bridges": [
    "b6a8cacd-abc6-4d24-993b-c363ea349e12"
  ],
  "talking_to": [
    "1446424814.22"
  ]
}

c.calls.answer(call['id'])
c.calls.hangup('call_id')
c.calls.hangup_from_user('call_id')   # Hangup calls of the authenticated user
c.calls.start_mute(call['id'])
c.calls.stop_mute(call['id'])
c.calls.send_dtmf_digits(call['id'], '1234567890*#')
c.calls.start_hold(call['id'])
c.calls.stop_hold(call['id'])
c.calls.start_record(call['id'])
c.calls.stop_record(call['id'])
c.calls.answer_from_user(call['id'])
c.calls.start_mute_from_user(call['id'])
c.calls.stop_mute_from_user(call['id'])
c.calls.send_dtmf_digits_from_user(call['id'], '1234567890*#')
c.calls.start_hold_from_user(call['id'])
c.calls.stop_hold_from_user(call['id'])
c.calls.start_record_from_user(call['id'])
c.calls.stop_record_from_user(call['id'])

c.calls.connect_user('call_id', 'user_uuid', timeout=15)

transfers = c.transfers.list_transfers_from_user()  # Lists transfers of the authenticated user
transfer = c.transfers.make_transfer(transferred='call_id',
                                     initiator='call_id',
                                     context='default',
                                     exten='1001',
                                     flow='blind',
                                     variables={'key': 'value'},
                                     timeout=15)
transfer = c.transfers.get_transfer(transfer['id'])
transfer = c.transfers.make_transfer_from_user(exten='1001', initiator='call-id', flow='blind', timeout=15)
transfer = c.transfers.get_transfer(transfer['id'])
c.transfers.cancel_transfer(transfer['id'])
c.transfers.cancel_transfer_from_user(transfer['id'])  # Cancel transfers of the authenticated user
c.transfers.complete_transfer(transfer['id'])
c.transfers.complete_transfer_from_user(transfer['id'])  # Complete transfers of the authenticated user

voicemail = c.voicemails.get_voicemail('my-voicemail-id')
voicemail = c.voicemails.get_voicemail_from_user()

calls = c.switchboards.list_queued_calls('my-switchboard-uuid')
new_call = c.switchboards.answer_queued_call_from_user('my-switchboard-uuid', 'a-call-id', line_id=1)
c.switchboards.hold_call('my-switchboard-uuid', 'a-call-id')
calls = c.switchboards.list_held_calls('my-switchboard-uuid')
new_call = c.switchboards.answer_held_call_from_user('my-switchboard-uuid', 'a-call-id', line_id=1)

relocate = c.relocates.create_from_user(initiator_call, destination, location, completions=['api'])
relocates = c.relocates.list_from_user()
relocate = c.relocates.get_from_user(relocate_uuid)
c.relocates.complete_from_user(relocate_uuid)
c.relocates.cancel_from_user(relocate_uuid)

application = c.applications.get('my-application-uuid')

call_args = {
    'context': 'my-context',
    'exten': '1001',
    'autoanswer': False,  # Defaults to False
}
call = c.applications.make_call(application['uuid'], call_args)
c.applications.answer_call(application['uuid'], call['id'])
c.applications.start_progress(application['uuid'], call['id'])
c.applications.stop_progress(application['uuid'], call['id'])
c.applications.start_hold(application['uuid'], call['id'])
c.applications.stop_hold(application['uuid'], call['id'])
c.applications.start_mute(application['uuid'], call['id'])
c.applications.stop_mute(application['uuid'], call['id'])
c.applications.start_moh(application['uuid'], call['id'], moh_uuid)
c.applications.stop_moh(application['uuid'], call['id'])

c.applications.send_playback(application['uuid'], call['id'], playback)
c.applications.delete_playback(application['uuid'], playback_uuid)

node = c.applications.create_node(application['uuid'], [call['id']])
call_args = {
    'user_uuid': 'my-user-uuid',
    'autoanswer': False,  # Defaults to False
}
call = c.applications.make_call_user_to_node(application['uuid'], node['uuid'], call_args)
call = c.applications.make_call_to_node(application['uuid'], node['uuid'], call_args)
c.applications.join_node(application['uuid'], node['uuid'], call['id'])
nodes = c.applications.list_nodes(application['uuid'])
node = c.applications.get_node(application['uuid'], node['uuid'])
c.applications.delete_node(application['uuid'], node['uuid'])
c.applications.delete_call_from_node(application['uuid'], node['uuid'], call['id'])

snooping_call_args = {
    'context': 'my-context',
    'exten': '1002',
    'autoanswer': True,
}
snooping_call = c.applications.make_call(application['uuid'], snooping_call_args)
snoop_args = {
    'snooping_call_id': snooping_call['id'],
    'whisper_mode': None,
}
snoop = c.applications.snoops(application['uuid'], call['id'], snoop_args)
c.applications.update_snoop(application['uuid'], snoop['uuid'], snoop_args)
c.applications.delete_snoop(application['uuid'], snoop['uuid'])
c.applications.get_snoop(application['uuid'], snoop['uuid'])
c.applications.list_snoop(application['uuid'])
c.applications.send_dtmf_digits(application['uuid'], call['id'], '1234567890*#')

participants = c.conferences.list_participants(conference_id)
participants = c.conferences.user_list_participants(conference_id)  # user may only list if participant himself
c.conferences.kick_participant(conference_id, participant_id)
c.conferences.mute_participant(conference_id, participant_id)
c.conferences.record(conference_id)
c.conferences.stop_record(conference_id)

c.faxes.send(pdf_content, context, extension, caller_id='number 12 <12>')

# This does the same thing, but derives the user UUID from the auth token
c.faxes.send_from_user(pdf_content, extension, caller_id='number 12 <12>')


# Endpoint status
lines = c.lines.list_lines()
trunks = c.trunks.list_trunks()

# Adhoc conferences
adhoc_conference = c.adhoc_conferences.create_from_user(
    host_call_id,
    participant1_call_id,
    participant2_call_id,
    ...
)
c.adhoc_conferences.delete_from_user(adhoc_conference_id)
c.adhoc_conferences.add_participant_from_user(adhoc_conference_id, call_id)
c.adhoc_conferences.remove_participant_from_user(adhoc_conference_id, call_id)

# Config
config = c.config.get()

config_patch = {
    'op': 'replace',
    'path': '/debug',
    'value': True,
}
c.config.patch(config_patch)


# Meetings
participants = c.meetings.list_participants(meeting_uuid)
participants = c.meetings.user_list_participants(meeting_uuid)  # user may only list if participant himself
c.meetings.kick_participant(meeting_uuid, participant_id)
c.meetings.user_kick_participant(meeting_uuid, participant_id)  # user may only kick if owner of the meeting


# Parkings
parked_call = {
  'slot': '701',
  'timeout_at': '2024-01-01T00:00:00',
}

parkings = c.parking_lots.list_()
parking = c.parking_lots.get('parking_id')
parked_call = c.calls.park('call_id',  # Park the call in selected parking
                           'parking_id',
                           preferred_slot='501',
                           timeout=30)
parked_call = c.calls.park_from_user('call_id',  # Park the user's connected call in selected parking
                                     'parking_id',
                                     preferred_slot='502',
                                     timeout=10)
```

## Running unit tests

```
pip install tox
tox --recreate -e py39
```

## How to implement a new command

Someone trying to implement a new command to the client would have to implement a new class, sub-classing the RESTCommand (available in wazo-lib-rest-client). The new class must be in the setup.py in the entry points under calld_client.commands. The name of the entry point is used as the handle on the client. For example, if your new entry point entry looks like this:

```python
entry_points={
    'calld_client.commands': [
        'foo = package.to.foo:FooCommand'
    ]
}
```

then your command will be accessible from the client like this:

```python
c = Client(...)

c.foo.bar()  # bar is a method of the FooCommand class
```
