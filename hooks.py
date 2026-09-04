import re

def get_topic_type(src_path):
    filename = src_path.split("/")[-1].lower()

    if filename.startswith("troubleshooting-"):
        return "Troubleshooting"
    if filename.startswith("example-"):
        return "Example"
    if "reference" in filename:
        return "Reference"
    if filename == "overview.md":
        return "Overview"
    if filename in ["index.md", "getting-started.md"]:
        return None

    return "Task"


def on_page_content(html, page, **kwargs):
    meta_html = ""

    topic_type = get_topic_type(page.file.src_path)

    if topic_type:
        meta_html += f'''
<span class="topic-type topic-type--{topic_type.lower()}">
  {topic_type}
</span>
'''

    if page.meta and page.meta.get("git_revision_date_localized"):
        revision = page.meta["git_revision_date_localized"]

        meta_html += f'''
<div class="page-revision-date">
  Last updated: {revision}
</div>
'''

    if meta_html:
        html = re.sub(
            r'(</h1>)',
            r'\1' + meta_html,
            html,
            count=1
        )

    if page.file.src_path != "index.md":
        feedback_html = '''
<div class="page-feedback">
  <span class="page-feedback__label">Was this helpful?</span>

  <div class="page-feedback__actions">
    <a class="feedback-button"
       href="mailto:YOUR-EMAIL@example.com?subject=Documentation%20feedback%20-%20Helpful">
      👍 Yes
    </a>

    <a class="feedback-button"
       href="mailto:YOUR-EMAIL@example.com?subject=Documentation%20feedback%20-%20Not%20helpful">
      👎 No
    </a>
  </div>
</div>
'''
        html += feedback_html

    return html
