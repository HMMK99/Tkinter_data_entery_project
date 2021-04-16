import csv
import os
import webbrowser

__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))
path = 'دفتر التردد.txt'
data = []
with open(os.path.join(__location__, path), 'r',
          encoding="utf-8") as dictfile:
    csv_reader = csv.DictReader(dictfile, delimiter=',')
    for line in csv_reader:
        data.append(line)

head = '''<!DOCTYPE html>
<html lang="ar">
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: right;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body style="text-align: center;">

<h2>HTML Table</h2>

<table>'''
with open(os.path.join(__location__, 'hist.html'), 'w',
          encoding="utf-8") as dictfile:
    # csv_writer = csv.DictWriter(dictfile,
    #                             fieldnames=field_names, delimiter=',')
    dictfile.write(head)
r_body = '''
</table>
<button onclick="window.print();" class="noPrint">
Print Me
</button>

</body>
</html>'''
with open(os.path.join(__location__, 'hist.html'), 'a',
          encoding="utf-8") as dictfile:
    field_names = ['اليوم',
                   'الوقت',
                   'بطاقة علاج رقم',
                   'الرقم داخل الهيئة',
                   'القسم',
                   'الإسم'
                   ]
    # csv_writer = csv.DictWriter(dictfile,
    #                             fieldnames=field_names, delimiter='</tr>')
    dictfile.write('<tr>')
    for label in field_names:
        dictfile.write('<th>')
        dictfile.write(label)
        dictfile.write('</th>')
        dictfile.write('\n')
    dictfile.write('</tr>')

    for row in range(len(data)):
        # print(data[row])
        if data[row]['الإسم'] != "رامي":
            continue
        dictfile.write('<tr>')
        for label in field_names:
            dictfile.write('<td>')
            dictfile.write(data[row][label])
            dictfile.write('</td>')
        dictfile.write('</tr>')
        dictfile.write('\n')
    dictfile.write(r_body)

url = os.path.join(__location__, 'hist.html')
webbrowser.open(url, new=2)
