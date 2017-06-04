import dictmerge

def test_best_effort_merge_overwrite():
    accumulated_dict = {'hello': 'world'}
    update_dict = {'hello': 3}
    assert dictmerge.best_effort_merge(accumulated_dict, update_dict) == {'hello': 3}


def test_best_effort_merge_add_missing_key():
    accumulated_dict = {'hello': 'world'}
    update_dict = {'abc': 'xyz'}
    assert dictmerge.best_effort_merge(accumulated_dict, update_dict) == {'hello': 'world', 'abc': 'xyz'}
    

def test_best_effort_merge_nested_overwrite():
    accumulated_dict = {'hello': {'world': 1}}
    update_dict = {'hello': 3}
    assert dictmerge.best_effort_merge(accumulated_dict, update_dict) == {'hello': 3}

def test_best_effort_merge_nested_overwrite2():
    accumulated_dict = {'hello': 'world', 'abc': 'xyz'}
    update_dict = {'hello': {'world': 1}}
    assert dictmerge.best_effort_merge(accumulated_dict, update_dict) == {'hello': {'world': 1}, 'abc': 'xyz'}
