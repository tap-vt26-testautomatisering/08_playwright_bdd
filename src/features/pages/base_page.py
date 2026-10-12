
class BasePage:
    def __init__(self, page):
        self.page = page
        self.add_players_button = page.get_by_role("button", name="Lägg till spelare")


    def navigate(self):
        self.page.goto("https://forverkliga.se/JavaScript/whose-turn/", timeout=10_000)

#x = BasePage()
