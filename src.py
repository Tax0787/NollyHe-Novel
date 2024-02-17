#dummy

from A import Element

#start

target, n = '''\
\
''', ()

now_page = 0

page, value = [], ''
for i, j in enumerate(target.split('<!-- \\n -->')):
  value += j
  if i == n:
    page.append(value)
    value = ''
else:
  if value != '':
    page.append(value)


def text_set(text):
  Element("text").element.innerText = text


def update():
  text_set(page[now_page])


update()


def event_last():
  global now_page
  now_page -= 1
  update()


def event_next():
  global now_page
  now_page += 1
  update()
