from asyncio import wait_for

from playwright.sync_api import Page, expect


def test_basic_duckduckgo_search(page: Page):
    page.goto("https://www.duckduckgo.com")
    page.locator('#searchbox_input').fill('tyrese haliburton')
    page.get_by_label("Search", exact=True).click()
    expect(page.locator('#search_form_input')).to_have_value('tyrese haliburton')
    page.get_by_test_id('result-title-a').nth(5).wait_for()
    titles = page.get_by_test_id('result-title-a').all_text_contents()
    matches = [title for title in titles if "haliburton" in title.lower()]
    assert len(matches) > 0, "No matches"
    pass
