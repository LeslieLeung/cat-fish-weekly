import os
import re
from typing import Tuple

import jinja2
import markdown

title_pattern = re.compile("^猫鱼周刊 (vol. (\d+) (.*?)).md$")
url_template = "https://ameow.xyz/archives/weekly-{}"


def get_title_and_url(filename: str) -> Tuple[str, str]:
    mg = title_pattern.match(filename)
    if mg is None:
        return filename, ""
    title = mg.group(1)
    issue = mg.group(2)
    url = url_template.format(issue)
    return title, url


issues = []

# iterate over all files in the issues directory
for filename in os.listdir("issues"):
    if not filename.endswith(".md"):
        continue

    # get metadata from markdown, get the issue and date
    with open(os.path.join("issues", filename)) as f:
        # title, url
        title, url = get_title_and_url(filename)
        # read all lines from the file
        lines = f.readlines()
        # concatenate all lines into a single string
        content = "".join(lines)
        # parse the markdown
        md = markdown.Markdown(extensions=["meta"])
        md.convert(content)
        # get the metadata
        issues.append(
            {
                "title": title,
                "date": md.Meta["date"][0],
                "issue": md.Meta["issue"],
                "url": url,
            }
        )

# order the issues by date in descending order
issues.sort(key=lambda x: x["date"], reverse=True)

template_loader = jinja2.FileSystemLoader(searchpath="./templates")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("readme.tmpl")
output = template.render(issues=issues)

with open("README.md", "w") as f:
    f.write(output)
