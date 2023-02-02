# Idea: periodically download the JSON, put it on the server and use that to serve content
import requests
import json
import clipboard
import html as h

r = requests.get(
    "https://itch.io/api/1/bynC96fBgH2lKpAPqekjR4hWF4J5rtT7U7A8PUpX/my-games"
)


class ItchIOGame:
    title = ""
    url = ""
    thumbnail_url = ""
    description = ""
    has_embed = False
    publish_date = ""
    platform_windows = False
    platform_mac = False
    platform_linux = False
    platform_android = False
    download_count = 0
    view_count = 0


# Title : [0:url, 1:html, 2:thumbnail_url, 3:description]
game_data = []

games_json = json.loads(r.content)
# print(json.dumps(games_json, indent=4))


for game_json in games_json["games"]:
    game = ItchIOGame()
    game.title = game_json["title"]
    game.url = game_json["url"]
    game.thumbnail_url = game_json["cover_url"]
    game.description = game_json["short_text"]
    game.has_embed = "embed" in game_json
    game.publish_date = game_json["published_at"][0:10]
    game.platform_windows = game_json["p_windows"]
    game.platform_mac = game_json["p_osx"]
    game.platform_linux = game_json["p_linux"]
    game.platform_android = game_json["p_android"]
    game.download_count = game_json["downloads_count"]
    game.view_count = game_json["views_count"]
    game_data.append(game)


# <GameEntry name="Game" url="www.google.com" imageSrc="https://img.itch.zone/aW1nLzIyNTM5NzcuZ2lm/315x250%23c/d%2BGB2n.gif" description="Prototype of a local co-op game for Fragment Jam." releaseDate="2019-07-04" web windows />
template = """<GameEntry name="#TITLE#" url="#URL#" imageSrc="#THUMB_URL#" description="#DESCRIPTION#" releaseDate="#RELEASE_DATE#" #PLATFORMS# />
"""

web = 'web '
win = 'windows '
mac = 'macos '
linux = 'linux '
android = 'android '

html = ""

for game in game_data:
    new = template

    platforms = ""
    if game.has_embed:
        platforms += web
    if game.platform_windows:
        platforms += win
    if game.platform_mac:
        platforms += mac
    if game.platform_linux:
        platforms += linux
    if game.platform_android:
        platforms += android

    new = new.replace("#TITLE#", game.title)
    new = new.replace("#RELEASE_DATE#", f"{game.publish_date}")
    new = new.replace("#THUMB_URL#", game.thumbnail_url)
    new = new.replace("#URL#", game.url)
    new = new.replace("#DESCRIPTION#", h.escape(game.description, True))
    new = new.replace("#PLATFORMS#", platforms)

    print(new)
    print("\n")
    html += new


html = '  <div class="columns is-multiline p-5 mx-4">' + html
html = html + "  </div>"
clipboard.copy(html)
print("------\nHTML copied to clipboard!")
