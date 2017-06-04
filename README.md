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

* Quick Perf
TL;DR - Not good :-|
```
In [1]:  accumulated_dict = {'x': {'whack': range(0,1000), 'bonk': range(0, 10000), 'properties': {'p1': 'mclaren', 'p50': 'peel'}}}

In [2]: update_dict = {'x': {'properties': {'p100D': 'Tesla'}}}

In [3]: from dictmerge import best_effort_merge

In [4]: %timeit best_effort_merge(accumulated_dict, update_dict)
10 loops, best of 3: 53.7 ms per loop <<<<<<<<<<<<<<<<<-------------- :-O

In [5]: x = best_effort_merge(accumulated_dict, update_dict)

In [6]: import json

In [7]: %timeit json.dumps(x)
100 loops, best of 3: 2.23 ms per loop

In [8]: json_x = json.dumps(x)

In [9]: %timeit json.loads(json_x)
100 loops, best of 3: 2.38 ms per loop

In [10]:
```
