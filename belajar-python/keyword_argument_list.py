def create_html(tag, text, **attributes):
    # print("attributes : ")
    # print(attributes)
    html = f"<{tag}"

    for key, val in attributes.items():
        html = html + f" {key}='{val}'"
    
    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "hallo python")
print(html)

html = create_html("a", "klik disini", href="www.google.com", style="link")
print(html)