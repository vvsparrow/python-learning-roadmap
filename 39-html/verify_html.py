with open("page.html", encoding="utf-8") as f:
    html_content = f.read()

assert "Capybara" in html_content
assert 'id="page-title"' in html_content
assert 'name="username"' in html_content
assert 'data-testid="search-area"' in html_content
assert 'src="capybara.jpeg"' in html_content

print("HTML structure and test locators verified successfully.")
