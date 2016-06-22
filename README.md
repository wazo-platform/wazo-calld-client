xivo-ctid-ng-client
===================

A python library to connect to xivo-ctid-ng. HTTPS is used by default. Certificates
are not verified by default. To check if the certificates are valid, use the
verify_certificate argument when instantiating the client.

Usage:

```python
from xivo_ctid_ng_client import Client

c = Client('localhost', token='the-one-ring', verify_certificate='</path/to/trusted/certificate>')

mycalls = c.calls.list_calls()

params = {
  "destination": {
    "extension": "8001",
    "context": "default",
    "priority": 1
  },
  "source": {
    "user": "ec008fd8-df3c-427a-8cb7-f94c1d238ad3"
  }
}

call = c.calls.make_call(params)
call = c.calls.make_from_user(extension='1234', variables={'key': 'value'})

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

c.calls.hangup('call_id')
c.calls.connect_user('call_id', 'user_uuid')

transfer = c.transfers.make_transfer(transferred='call_id',
                                     initiator='call_id',
                                     context='default',
                                     exten='1001',
                                     flow='blind',
                                     variables={'key': 'value'})
transfer = c.transfers.get_transfer(transfer['id'])
c.transfers.cancel_transfer(transfer['id'])
c.transfers.complete_transfer(transfer['id'])

```

## Tests

Running unit tests
------------------

```
pip install tox
tox --recreate -e py27
```

## How to implement a new command

Someone trying to implement a new command to the client would have to implement
a new class, sub-classing the RESTCommand (available in
xivo-lib-rest-client). The new class must be in the setup.py in the entry points
under ctid_ng_client.commands. The name of the entry point is used as the handle on
the client. For example, if your new entry point entry looks like this:

```python
entry_points={
    'ctid_ng_client.commands': [
        'foo = package.to.foo:FooCommand'
    ]
}
```

then your command will be accessible from the client like this:

```python
c = Client(...)

c.foo.bar()  # bar is a method of the FooCommand class
```
