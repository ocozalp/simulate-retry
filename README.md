# simulate-retry
Just trying something

## Runtime Test Results

### Big Interval (1000000), 1000 Small Events([100, 200])

|Data Structure|Result(secs)|
|--------------|------------|
|Dummy         |0.0869      |
|Fenwick Tree  |0.1010      |

### Medium Interval (100000), 20000 Long Events([900, 1000])

|Data Structure|Result(secs)|
|--------------|------------|
|Dummy         |1.9600      |
|Fenwick Tree  |0.1275      |

### Big Interval (1000000), 100000 Events With a Big Range of Duration ([100, 10000])

|Data Structure|Result(secs)|
|--------------|------------|
|Dummy         |51.5447     |
|Fenwick Tree  |0.7408      |