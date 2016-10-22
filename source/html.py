import webbrowser

f = open('../output/130010006.html','w')

text = """<html>
<body>
<video width="429" height="298" controls autoplay loop>
  <source src="130010006.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
</body>
</html>"""

f.write(text)
f.close()