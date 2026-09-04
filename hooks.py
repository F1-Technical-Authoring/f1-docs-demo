import re

def on_page_content(html, page, **kwargs):
    # Add revision date under the H1
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

    # Add feedback to all pages except the homepage
    if page.file.src_path != "index.md":
        feedback_html = '''
<div class="page-feedback">
  <span class="page-feedback__label">Was this helpful?</span>

  <div class="page-feedback__actions">
    <a class="feedback-button"
       href="mailto:heather.firth@outlook.com?subject=Documentation%20feedback%20-%20Helpful">
      👍 Yes
    </a>

    <a class="feedback-button"
       href="mailto:heather.firth@outlook.com?subject=Documentation%20feedback%20-%20Not%20helpful">
      👎 No
    </a>
  </div>
</div>
'''

        html += feedback_html

    return html
