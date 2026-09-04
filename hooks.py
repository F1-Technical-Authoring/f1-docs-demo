import re

def on_page_content(html, page, **kwargs):
    if page.meta and page.meta.get("git_revision_date_localized"):
        revision = page.meta["git_revision_date_localized"]

        date_html = f'''
<div class="page-revision-date">
  Last updated: {revision}
</div>
'''

        html = re.sub(
            r'(</h1>)',
            r'\1' + date_html,
            html,
            count=1
        )

    return html
