import re

from dask.utils import byte_sizes
	

def parse_size(size):
    """
    Parse size string into number of bytes.

    :param: size [string]
    :return: integer (number of bytes)
    """
    try:
        n, suffix = re.match('^(\d+\.?\d*)([a-zA-Z]+)$', size).groups()
        multiplier = byte_sizes[suffix.lower()]

        size_in_bytes = multiplier * float(n)
    except KeyError as e:
        raise ValueError(f"Could not interpret '{suffix}' as a byte unit") 

    return size_in_bytes


