import re

def validate_url(url, params_to_remove=[]):
    # Use "r" string prefix to tell python interpreter to use raw strings. That way, it won't convert special codes like '\b'.
    search = re.search(r'^(((?:w{3}\.)*\w+\.)(\w+))\?*', url)
    validated_url = search.group(1)
    domain_suffix = search.group(3)

    # Replace non .gov domain suffixes
    if (re.match(r'gov.*', domain_suffix) is None):
        validated_url = "".join([search.group(2) + "gov"])

    param_searcher = re.finditer(r'(?:\?|\&)(?:(\w+)=(\w+))', url)
    added_params = {}
    all_params = []

    for match in param_searcher:
        param = match.group(1)
        all_params.append(param)
        value = match.group(2)
        if (param not in params_to_remove):
            added_params[param] = value
    if added_params:
        param_string = "&".join(['{param}={value}'.format(param=param, value=added_params[param]) for param in added_params])
        if not all([(p in all_params) for p in params_to_remove]):
            param_string = ""
        validated_url = "?".join([validated_url, param_string])

    return validated_url
