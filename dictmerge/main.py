def best_effort_merge(accumulated_dict, update_dict):
    """
    Best effort merge. Attempt to preserve elements in the
    aggregated dictionary if the types match. 
    *** Important - This function has side effects ***
    :param accumulated_dict: Aggregated dictionary
    :param update: Dict update to be added on
    :return: accumulated_dict with updates added in
    """
    for key, value in update_dict.iteritems():
        key_not_present = key not in accumulated_dict
        key_present_but_both_values_are_not_dicts = \
            (key in accumulated_dict) and \
            not (isinstance(value, dict) and isinstance(accumulated_dict.get(key), dict))

        # Base Case : Add the key value pair from the update_dict
        # to the accumulated_dict.
        if key_not_present or key_present_but_both_values_are_not_dicts:
            accumulated_dict[key] = value
        else:
            # Recursive Case : If the value is a dict, then recurse
            accumulated_dict[key] = best_effort_merge(accumulated_dict[key], value)

        return accumulated_dict
