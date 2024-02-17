from mn_format import decoding as d
from sys import argv as a


def getForm(src, n, title):
  return f'''<!DOCTYPE html>
<html>
	<head>
		<meta charset = "utf-8" />
		<title> {title} </title>
		<link rel = "stylesheet" type = "text/css" href = "style.css" />
		<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
		<script defer src="https://pyscript.net/alpha/pyscript.js"></script>
	</head>
	<body>
		<div id = "text"><div>
		<div class="container center">
			<button id = "last" pys-onClick = "event_last"> &lt;-- [ last - page ] </button>
			<p>|----------------|<p>
			<button id = "nect" pys-onClick = "event_next"> [ next - page ] --&gt; </button>
		</div>

		<py-script>
		  target, n = \'\'\'{src}\'\'\', {n}

			now_page = 0

			page, value = [], ''
			for i, j in enumerate(target.split('\n')):
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

		</py-script>
	</body>
</html>'''


def file2html(f):
  with open(f) as fp:
    src, n = decoding(fp.read())
  fn = f.split('.')
  fn.pop()
  fn = '.'.join(fn)
  with open(fn + '.html', 'w') as fp:
    fp.write(getForm(src, n, fn))


def main():
  file2html(a[1])


if __name__ == "__main__": main()
