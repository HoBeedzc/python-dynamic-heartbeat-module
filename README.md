# python-dynamic-heartbeat-module

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Usage

```python
import time
from dynamic_heartbeat import heartbeat as dhb

interval = dhb.Timer(default=10, min_=1, max_=60)
time.sleep(interval(True))  # True to slow down the heartbeat. 5s -> 10s
time.sleep(interval(False))  # False to speed up the heartbeat. 5s -> 2.5s
```
