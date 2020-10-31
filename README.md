# TEAM SO GOOD
The value of this solution is to provide flexible integrated functionality for variety of end devices, IoT sensor alert, camera etc. with industrial worker’s communication.

![overview](docs/overview.png)

## Getting Start
### Requirement
- python: 3.8.5
- python library
  - requests
  - pyyaml

## Configuration
If you want to add the sensors you want to monitor, add them to hosts.yaml.

```
sensors:
- <sensor name>: <ip address>
```

## Usage
```
git clone https://github.com/yukamoja/team-so-good
cd team-so-good
python retrieve.py
```

# License
BSD licensesis freely redistributable under the BSD 2 clause license. Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.