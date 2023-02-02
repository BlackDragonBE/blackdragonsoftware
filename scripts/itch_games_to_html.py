# Idea: periodically download the JSON, put it on the server and use that to serve content
import requests
import json
import clipboard

r = requests.get("https://itch.io/api/1/bynC96fBgH2lKpAPqekjR4hWF4J5rtT7U7A8PUpX/my-games")


class ItchIOGame:
    title = ''
    url = ''
    thumbnail_url = ''
    description = ''
    has_embed = False
    publish_date = ''
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


for game_json in games_json['games']:
  game = ItchIOGame()
  game.title = game_json['title']
  game.url = game_json['url']
  game.thumbnail_url = game_json['cover_url']
  game.description = game_json['short_text']
  game.has_embed = 'embed' in game_json
  game.publish_date = game_json['published_at'][0:10]
  game.platform_windows = game_json['p_windows']
  game.platform_mac = game_json['p_osx']
  game.platform_linux = game_json['p_linux']
  game.platform_android = game_json['p_android']
  game.download_count = game_json['downloads_count']
  game.view_count = game_json['views_count']
  game_data.append(game)


template = """<div class="column is-one-third is-2-desktop">
        <div class="card">
          <figure class="image image is-16by9 is-fullwidth">
            <a href="#URL#"><img src="#THUMB_URL#" style="object-fit: contain;background-color: black;">            
            </a>
          </figure>
          <div class="media-content p-2">
            <div>
              #PLATFORMS#
            </div>
            <a href="#URL#" class="is-size-5">#TITLE#</a><br>
            <h2 class="subtitle is-size-6">#SUBTITLE#</h2>
            <p>#DESCRIPTION#</p>

          </div>
        </div>
      </div>"""

icon_web = '<i class="fab fa-chrome fa-fw"></i>'
icon_win = '<i class="fab fa-windows fa-fw"></i>'
icon_mac = '<i class="fab fa-apple fa-fw"></i>'
icon_linux = '<i class="fab fa-linux fa-fw"></i>'
icon_android = '<i class="fab fa-android fa-fw"></i>'

html = ''

for game in game_data:
    new = template

    platform_icons_html = ''
    if game.has_embed: platform_icons_html += icon_web
    if game.platform_windows: platform_icons_html += icon_win
    if game.platform_mac: platform_icons_html += icon_mac
    if game.platform_linux: platform_icons_html += icon_linux
    if game.platform_android: platform_icons_html += icon_android

    new = new.replace('#TITLE#', game.title)
    new = new.replace('#SUBTITLE#', f"Released on itch.io on {game.publish_date}")
    new = new.replace('#THUMB_URL#', game.thumbnail_url)
    new = new.replace('#URL#', game.url)
    new = new.replace('#DESCRIPTION#', game.description)
    new = new.replace('#PLATFORMS#', platform_icons_html)
    # new = new.replace('#DESCRIPTION#', game_data[gd][3])
    print(new)
    print('\n')
    html += new


html = '  <div class="columns is-multiline p-5 mx-4">' + html
html = html + '  </div>'
clipboard.copy(html)
print('------\nHTML copied to clipboard!')


