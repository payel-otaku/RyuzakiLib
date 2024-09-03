import wget
from RyuzakiLib.api.reqs import async_search


class PornoHub:
    def __init__(self, base_api_dev: str = "https://xyz69-ryuzaki-api.hf.space"):
        self.base_api_dev = base_api_dev

    async def x_search(self, query=None, quality="720p", results=15):
        url = f"{self.base_api_dev}/akeno/xnxxsearch?query={query}&quality={quality}&results={results}"
        res = await async_search(url, re_json=True)
        results = res["randydev"]["results"]
        y = res["randydev"]["results"][0]
        link = y["url"]
        title = y["title"]
        return [link, title, results]

    async def x_download(self, query=None, url=None, is_stream=False):
        if is_stream and url:
            url_ = f"{self.base_api_dev}/akeno/xnxx-dl?link={url}"
            response = await async_search(url_, re_json=True)
            file_path = wget.download(response["randydev"]["results"]["link"])
            thumb = wget.download(response["randydev"]["results"]["thumb"])
            title = response["randydev"]["results"].get("title", "Powered by Randydev")
            return file_path, thumb, title
        else:
            schub = await self.x_search(query=query)
            url_dl = f"{self.base_api_dev}/akeno/xnxx-dl?link={schub[0]}"
            response = await async_search(url_dl, re_json=True)
            file_path = wget.download(response["randydev"]["results"]["link"])
            thumb = wget.download(response["randydev"]["results"]["thumb"])
            title = response["randydev"]["results"].get("title", "Powered by Randydev")
            return file_path, thumb, title
