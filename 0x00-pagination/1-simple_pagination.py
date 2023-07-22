#!/usr/bin/env python3
""" 1. Simple pagination """

import csv
import math
from typing import List, Tuple

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

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ takes two integer arguments page with default value 1 and page_size with default value 10.
        Args:
            page (int): Page's Number requested.
            page_size (int): Records number to retrieve.

        Returns:
            List[List] List of Records which are List also.
        """
        assert isinstance(page, int) and page > 0, "page should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size should be a positive integer"
        
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.dataset()):
            return []
        
        return self.dataset()[start_index:end_index]
