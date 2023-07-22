#!/usr/bin/env python3
""" 0. Simple helper function """

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns a tuple of size two containing a start index and an end index corresponding to the range of indexes.

          Args:
                  page (int): Requested page to return.
                  page_size (int): Size of the page requested.
          Returns:
                  Tuple[int, int]: Segement of requested list (items).
          """
    startIndex = (page - 1) * page_size
    endIndex = page * page_size
    return (startIndex, endIndex)
