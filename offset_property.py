#!/usr/bin/python3
import argparse
from waapi import WaapiClient

parser = argparse.ArgumentParser(description='Increase or lower the volume of the objects.')
parser.add_argument('id', nargs='+', help='An object ID (GUID)')
parser.add_argument("-p", "--property", default='Volume', help="Specify the property to modify (default='Volume')")
parser.add_argument("-o", "--offset", type=float, default=1, help="Specify the offset to apply (default=1)")
args = parser.parse_args()

# Connect (default URL)
client = WaapiClient()

# Retrieve the volumes for the selected objects
query = { 'from': { 'id': args.id }}
options = { 'return': ['id', '@'+args.property]}
result = client.call("ak.wwise.core.object.get", query, options=options)

client.call("ak.wwise.core.undo.beginGroup")

# Set new volumes
for object in result['return']:
    setPropertyArgs = {
        'object': object['id'],
        'property': args.property,
        'value': object['@' + args.property] + args.offset
        }
    client.call("ak.wwise.core.object.setProperty", setPropertyArgs)

client.call("ak.wwise.core.undo.endGroup",displayName='Offset '+args.property)

# Disconnect
client.disconnect()