
from .base import BaseHandler, route


@route('/?')
class IndexHandler(BaseHandler):

    def get(self):
        self.render_md_file('index.md', 'smug api')


