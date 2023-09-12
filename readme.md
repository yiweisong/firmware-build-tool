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

## combined binary structure
/******** start *********/

configuration length

*************************

configuration json content

*************************

First Binary Content

*************************

Second Binary Content

*************************

....

*************************

Last Binary Content

/********* end **********/

## configuration json example
```javascript
const config = {
  content1: { size: 384, beginAddress: 0x08000000 },
  content2: { size: 312, beginAddress: 0x08003000, isBootloader: true },
  ...
  content3: { size: 4, beginAddress: 0x083ff000 },
};
```