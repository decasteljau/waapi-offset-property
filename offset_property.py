#!/usr/bin/python3
import argparse
from waapi import WaapiClient

parser = argparse.ArgumentParser(
    description='Offset a property value for a list of objects. '
    'By default, it increases the volume of the specified objects.')
parser.add_argument('id', nargs='+', help='An object ID (GUID)')
parser.add_argument("-p", "--property", default='Volume',
                    help="specify the property name to modify (default=Volume)")
parser.add_argument("-o", "--offset", type=float, default=1,
                    help="specify the offset value to apply (default=1)")
args = parser.parse_args()

accessor = '@'+args.property

# Connect (default URL)
with WaapiClient() as client:

    # Retrieve the volumes for the selected objects
    query = {'from': {'id': args.id}}
    options = {'return': ['id', accessor]}
    result = client.call("ak.wwise.core.object.get", query, options=options)

    # Make sure all of our set property calls are regrouped undo a single undo
    client.call("ak.wwise.core.undo.beginGroup")

    # Set new volumes
    for object in result['return']:
        if accessor in object:
            setPropertyArgs = {
                'object': object['id'],
                'property': args.property,
                'value': object[accessor] + args.offset
            }
            client.call("ak.wwise.core.object.setProperty", setPropertyArgs)

    client.call("ak.wwise.core.undo.endGroup",
                displayName='Offset '+args.property)
