import bleach
from bleach_whitelist.bleach_whitelist import markdown_tags, markdown_attrs
from markdown import Markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

md = Markdown(extensions=[GithubFlavoredMarkdownExtension()], output_format='html5')
markdown_tags.append('del')


def render_markdown(text):
    return bleach.clean(md.convert(text), tags=markdown_tags, attributes=markdown_attrs)
