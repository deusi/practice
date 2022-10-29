# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        allUrls = set()
        hostname = startUrl.split('/')[2]
        queue = collections.deque([startUrl])
        while queue:
            url = queue.popleft()
            if url.split('/')[2] != hostname or url.split('/')[2] in allUrls:
                continue
            allUrls.add(url)
            for newUrl in htmlParser.getUrls(url):
                if newUrl not in allUrls:
                    queue.append(newUrl)
        return list(allUrls)
        