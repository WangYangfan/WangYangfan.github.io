import markdown
import sys
import codecs
css0 = '''<!DOCTYPE html>
<html lang=en>
<head>
    <title>'''
css1 = '''</title>
    <meta charset="utf-8">
    <style>
        body {
            font-family: Cambria, STXihei, serif;
            font-size: 20px;
        }
    </style>
</head>
<body>
'''
css2 = '''
</body>
</html>'''
name = sys.argv[1]
in_file = '%s.md' % (name)
in_file = "./docs/"+in_file
out_file = '%s.html' % (name)
out_file = "./docs/"+out_file
md = codecs.open(in_file, mode="r", encoding="utf-8")
html = markdown.markdown(md.read())
output_file = codecs.open(out_file, "w", encoding="utf-8")
name = name + " - WangYangfan"
output_file.write(css0+name+css1+html+css2)
# output_file.write(html)