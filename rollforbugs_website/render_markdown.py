import bleach
from bleach_whitelist import bleach_whitelist
from markdown import Markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

md = Markdown(extensions=[GithubFlavoredMarkdownExtension()], output_format='html5')
bleach_whitelist.markdown_tags.append('del')


def render_markdown(text):
    return bleach.clean(md.convert(text), tags=bleach_whitelist.markdown_tags, attributes=bleach_whitelist.markdown_attrs)
