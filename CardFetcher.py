import re
from WikiaHandler import WikiaHandler


class CardFetcher:
    def __init__(self):
        self.url_pattern = re.compile("^cardfight\.wikia.com/wiki/[^/\s]*$")
        self.wikia_handler = WikiaHandler()

    def get_card_by_url(self, url):
        if not url.startswith("http://"):
            url = "http://" + url
        return self.wikia_handler.get_card_info_by_url(url)

    def format_effect(self, effect):
        effect = effect.strip()
        effect = effect.replace("<br>", "\n")
        effect = effect.replace("<br/>", "\n")
        effect = effect.replace("<b>", "**")
        effect = effect.replace("</b>", "**")
        effect = effect.replace("<i>", "*")
        effect = effect.replace("</i>", "*")
        return effect

    def format_card(self, card_info):
        print(card_info)
        if card_info is not None:
            effect = self.format_effect(card_info['Effect'])
            name = "[" + card_info['Name'] + "](" + "img url" + ")"
            wikia = "[wikia](" + card_info['Url'] + ")"
            card_text = (name + " " + wikia + "\n" +
                        card_info['Grade / Skill'] + " / " + card_info['Unit Type'] + "\n" +
                        "Power " + card_info['Power'] + " / Shield " + card_info['Shield'] + "\n" +
                         card_info['Clan'] + " / " + card_info['Race'] + "\n" +
                         "\n" + effect
                        )
            return card_text
        return "hi"

    def fetch_card(self, card_name: str):
        card_info = None
        if re.match(self.url_pattern, card_name):
            # If we've got a URL, just use that
            assert isinstance(card_name, str)
            card_info = self.get_card_by_url(card_name)
        else:
            # Else, we just use the name
            card_info = self.wikia_handler.get_card_info_by_name(card_name)

        return self.format_card(card_info)
