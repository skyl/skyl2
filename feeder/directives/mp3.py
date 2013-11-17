from docutils import nodes
from docutils.parsers.rst import Directive

CODE = """
<audio class="mp3-embed" controls>
  <source src="%(path)s" type="audio/mpeg">
  <embed height="50" width="100" src="%(path)s">
</audio>
"""


class MP3(Directive):
    """
    Source code syntax hightlighting.
    """
    required_arguments = 1
    has_content = False

    def run(self):
        string_vars = {
            'path': self.arguments[0],
        }
        return [nodes.raw('', CODE % (string_vars), format='html')]
