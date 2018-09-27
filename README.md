# Wwise Offset Property

This script offsets a property value for a list of Wwise objects. By default, it increases the volume of the specified objects. the script takes a list of object IDs.

## Requirements

* Python 3.6+ (see https://pypi.org/project/waapi-client/)

## Usage

```
usage: offset_property.py [-h] [-p PROPERTY] [-o OFFSET] id [id ...]

Offset a property value for a list of objects. By default, it increases the
volume of the specified objects.

positional arguments:
  id                    An object ID (GUID)

optional arguments:
  -h, --help            show this help message and exit
  -p PROPERTY, --property PROPERTY
                        specify the property name to modify (default=Volume)
  -o OFFSET, --offset OFFSET
                        specify the offset value to apply (default=1)
```

Refer to the [Wwise Objects Reference](https://www.audiokinetic.com/library/edge/?source=SDK&id=wobjects__index.html) for the list of properties available per object type.

## Example

### Increase the make-up gain by 2
```
py offset_property.py "{7BE98EBA-AF1C-4D1B-99B8-D6E8AED51929}" "{2892D2CD-05B8-46F5-A65E-5BBA435554EF}" -p MakeUpGain -o 2
```

## Wwise Command Add-on Setup

Using Wwise 2018.1.2 or higher
1. Copy the file `offset_property_commands.json` to:
    * **Windows**: %appdata%\Audiokinetic\Wwise\Add-ons\Commands
    * **Mac**: /Users/brodrigue/Library/Application Support/Wwise2018/Bottles/wwise/drive_c/users/crossover/Application Data/Audiokinetic/Wwise/Add-ons/Commands
1. Fix the path to `offset_property.py`
1. Restart Wwise
1. Select objects, and use the keys `-` or `=` to increase or decrease volume.
