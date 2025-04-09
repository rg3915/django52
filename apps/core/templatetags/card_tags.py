from django import template
from django.utils.html import format_html


register = template.Library()


@register.simple_block_tag(takes_context=True)
def card(context, content, header, footer):
    format_kwargs = {
        "header": header,
        "content": content,
        "footer": footer,
    }
    result = """
    <article>
      <header>{header}</header>
      {content}
      <footer>{footer}</footer>
    </article>
    """
    return format_html(result, **format_kwargs)
