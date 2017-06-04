# dict_merge
Simple utility to merge nested python dictionaries

## Testing
* Running all the tests
```
python setup.py test
```

* Running a specific test
```
python setup.py test --addopts='-s path/to/test.py::test_fn_name
```

## Quick Perf
### Before - With `copy.deepcopy`
TL;DR - Not good :-|
```
In [1]:  accumulated_dict = {'x': {'whack': range(0,1000), 'bonk': range(0, 10000), 'properties': {'p1': 'mclaren', 'p50': 'peel'}}}

In [2]: update_dict = {'x': {'properties': {'p100D': 'Tesla'}}}

In [3]: from dictmerge import best_effort_merge

In [4]: %timeit best_effort_merge(accumulated_dict, update_dict)
10 loops, best of 3: 53.7 ms per loop <<<<<<<<<<<<<<<<<-------------- :-O
```

### After - No `copy.deepcopy`
TL;DR - :thumbsup: :shipit:
```
In [1]:  accumulated_dict = {'x': {'whack': range(0,1000), 'bonk': range(0, 10000), 'properties': {'p1': 'mclaren', 'p50': 'peel'}}}

In [2]: update_dict = {'x': {'properties': {'p100D': 'Tesla'}}}

In [3]: from dictmerge import best_effort_merge

In [4]: %timeit best_effort_merge(accumulated_dict, update_dict)
100000 loops, best of 3: 4.94 µs per loop <<<<<<<<<<<<<<<---------- :-)

```
	
