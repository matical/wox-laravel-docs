import re
import textwrap
import webbrowser

from algoliasearch import algoliasearch

from wox import Wox


class LaravelDocs(Wox):
    def query(self, query: str):
        if not query:
            return

        if re.findall(r'^([5]\.[0-6]):', query):
            self.branch = query[:3]
            to_search = query[4:]
        else:
            self.branch = 'master'
            to_search = query

        return [self.build_payload(found) for found in self.search(to_search)]

    def open_url(self, url: str):
        webbrowser.open_new_tab(url)

    def search(self, query: str) -> list:
        return self.build_algolia_client().search(query, {'tagFilters': [self.branch]})['hits']

    def build_payload(self, result) -> dict:
        return {
            "Title": self.title(result),
            "SubTitle": self.subtitle(result),
            "IcoPath": "Images\\app.png",
            "JsonRPCAction": {
                "method": "open_url",
                "parameters": [self.build_url(result['link'])],
            }
        }

    def build_algolia_client(self) -> algoliasearch.Index:
        return algoliasearch.Client(
            '8BB87I11DE', '8e1d446d61fce359f69cd7c8b86a50de'
        ).init_index('docs')

    def build_url(self, link) -> str:
        return f'https://laravel.com/docs/{self.branch}/{link}'

    def title(self, segment) -> str:
        if segment['h2']:
            return f"{segment['h1']} » {segment['h2']}"

        return segment['h1']

    def subtitle(self, segment) -> str:
        if segment['h4']:
            return segment['h4']

        if segment['h3']:
            return segment['h3']

        if segment['h2'] and 'content' in segment['_highlightResult']:
            content = segment['_highlightResult']['content']['value']
            cleaned = re.sub('<[^<]+?>', '', content)

            return textwrap.shorten(cleaned, width=150, placeholder='...')

        return self.build_url(segment['link'])


if __name__ == "__main__":
    LaravelDocs()
