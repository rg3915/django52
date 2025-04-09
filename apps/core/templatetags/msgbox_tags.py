from django import template
from django.utils.html import format_html


register = template.Library()


@register.simple_block_tag(takes_context=True)
def msgbox(context, content, level):
    format_kwargs = {
        "level": level.lower(),
        "level_title": level.capitalize(),
        "content": content,
        "open": " open" if level.lower() == "error" else "",
        "site": context.get("site", "My Site"),
    }
    result = """
    <div class="msgbox {level}">
      <details{open}>
        <summary>
          <strong>{level_title}</strong>: Please read for <i>{site}</i>
        </summary>
        <p>
          {content}
        </p>
      </details>
    </div>
    """
    return format_html(result, **format_kwargs)
