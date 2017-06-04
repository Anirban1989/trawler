from trawler.browsers import BrowseBing, BrowseStackOverFlow
from trawler.browsers.exceptions import BrowerScrapeMethodNotImplemented
import pytest


def test_browse_with_bing():
    bing = BrowseBing(kw="Ravi RT Merugu", max_page=1)
    bing.search()
    result = bing.data
    assert type(result) is dict
    assert "results" in result
    assert "related_keywords" in result
    bing.close()


def test_browser_with_stackoverflow():
    stack = BrowseStackOverFlow(kw="Python Exception errors", max_page=1)
    stack.search()
    result = stack.data
    assert type(result) is dict
    assert "results" in result
    assert "related_keywords" in result
    stack.close()
    

def test_browser_no_nextpage():
    bing = BrowseBing(kw="XxXXXXXXxxxxxbas dans dsand msad asd amd ansd am dna smda sdn asdmas dm", max_page=1)
    bing.search()
    result = bing.data
    assert result['next_url'] is None
    bing.close()


def test_browser_implamentation_error():
    bing = BrowseBing(kw="Hello", max_page=1, method="chromejjj")
    with pytest.raises(BrowerScrapeMethodNotImplemented) as excinfo:
        bing.search()
    assert "Not implemented" in str(excinfo)
    bing.close()
