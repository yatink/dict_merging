from copy import deepcopy

def best_effort_merge(accumulated_dict, update_dict):
    """
    Best effort merge. Attempt to preserve elements in the
    aggregated dictionary if the types match. 
    :param accumulated_dict: Aggregated dictionary
    :param update: Dict update to be added on
    :return: New dictionary with updates added in
    """
    ad = deepcopy(accumulated_dict)

    for key, value in update_dict.iteritems():
        key_not_present = key not in ad
        key_present_but_both_values_are_not_dicts = \
            (key in ad) and not all(isinstance(x, dict) for x in [value, ad.get(key)])

        # Base Case : Add the key value pair from the update_dict
        # to the accumulated_dict.
        if key_not_present or key_present_but_both_values_are_not_dicts:
            ad[key] = value
        else:
            # Recursive Case : If the value is a dict, then recurse
            ad[key] = best_effort_merge(ad[key], value)

        return ad
