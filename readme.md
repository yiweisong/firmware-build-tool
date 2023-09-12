# A firmware build tool

## prepare
Move the binary files to bin folder. Then prepare a configuration file.

## usage
```python
python3 main.py
```

## startup args
| Name | Type | Default | Description |
| - | :-: | :-: | - |
| -n | String | 'combined.bin' | Specify the combined file name |
| -b | String | './bin' | Specify the binary files container |
| -c | String | 'config.cfg' | Specify the configuration file |