import os

from docutils import nodes
from docutils.parsers.rst import Directive


NODE = """
<div class="margin0auto venn{0}"></div>
<script src="//cdnjs.cloudflare.com/ajax/libs/d3/3.3.10/d3.min.js"></script>
<script src="/static/js/directives/venn.js"></script>
<script>
{content}
sets = venn.venn(sets, overlaps);
venn.drawD3Diagram(d3.select(".venn{0}"), sets, {width}, {height});
</script>
"""

class Venn(Directive):
    """
    Source code syntax hightlighting.
    """
    required_arguments = 0
    optional_arguments = 0
    has_content = True

    def run(self):
        self.assert_has_content()
        clas = os.urandom(4).encode('hex')
        full = NODE.format(
            clas, width=300, height=300,
            content="".join(self.content),
        )
        return [nodes.raw("", full, format="html")]
