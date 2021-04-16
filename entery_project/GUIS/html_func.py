import csv
import os
import webbrowser
import re
from functions import search_date_for_search
from datetime import datetime

__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))


def creat_html(target_name, new=False):
    head = '''<!DOCTYPE html>
        <html lang="ar">
        <head>
        <style>
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 90%;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: right;
            padding: 8px;
        }

        tr:nth-child(even) {
            background-color: #bbbbbb;
        }
        </style>
        </head>
        <body style="text-align: center;background-color: #eeeeee;">

        <h2>''' + target_name + '''</h2>

        <table style="margin-right: 30px;margin-left: 30px;">'''
    with open(os.path.join(__location__, target_name+'.html'), 'w',
              encoding="utf-8") as dictfile:
        dictfile.write(head)

    with open(os.path.join(__location__, target_name+'.html'), 'a',
              encoding="utf-8") as dictfile:
        field_names = ['اليوم',
                       'الوقت']
        if new:
            field_names.append('محول من')
            field_names.append('اسم المسجل')
        else:
            field_names.append('دفتر')
        field_names.append('بطاقة علاج رقم')
        field_names.append('الرقم داخل الهيئة')
        field_names.append('القسم')
        field_names.append('الإسم')
        dictfile.write('<tr>')
        for label in field_names:
            dictfile.write('<th>')
            dictfile.write(label)
            dictfile.write('</th>')
            dictfile.write('\n')
        dictfile.write('</tr>')


def end_html(target_name):
    with open(os.path.join(__location__, target_name+'.html'), 'a',
              encoding="utf-8") as dictfile:
        r_body = '''
        </table>
        <button onclick="window.print();" class="noPrint">
        Print Me
        </button>

        </body>
        </html>'''
        dictfile.write(r_body)


def add_data_to_html(data, target_name, new=False):
    with open(os.path.join(__location__, target_name+'.html'), 'a',
              encoding="utf-8") as dictfile:
        field_names = ['اليوم',
                       'الوقت']
        if new:
            field_names.append('محول من')
            field_names.append('اسم المسجل')
        else:
            field_names.append('دفتر')
        field_names.append('بطاقة علاج رقم')
        field_names.append('الرقم داخل الهيئة')
        field_names.append('القسم')
        field_names.append('الإسم')
        if data:
            for row in range(len(data)):
                dictfile.write('<tr>')
                for label in field_names:
                    dictfile.write('<td>')
                    if not data[row][label]:
                        data[row][label] = 'None'
                    dictfile.write(data[row][label])
                    dictfile.write('</td>')
                dictfile.write('</tr>')
                dictfile.write('\n')


def read_file(path):
    data = []
    with open(os.path.join(__location__, path), 'r',
              encoding="utf-8") as dictfile:
        csv_reader = csv.DictReader(dictfile, delimiter=',')
        for line in csv_reader:
            data.append(line)
        return data


def render_table(target_name):
    url = os.path.join(__location__, target_name+'.html')
    webbrowser.open(url, new=2)


def update_table(line, target_name, new=False):
    '''
    this function update the html table by finding the closing table tag.
    then replace it with updated data.
    '''
    with open(os.path.join(__location__, target_name+'.html'), 'r+',
              encoding="utf-8") as dictfile:
        print(line)
        field_names = ['اليوم',
                       'الوقت']
        if new:
            field_names.append('محول من')
            field_names.append('اسم المسجل')
        else:
            field_names.append('دفتر')
        field_names.append('بطاقة علاج رقم')
        field_names.append('الرقم داخل الهيئة')
        field_names.append('القسم')
        field_names.append('الإسم')
        new_line = '<tr>'
        for label in field_names:
            new_line += '<td>'
            new_line += str(line[label])
            new_line += '</td>'
        new_line += '</tr>\n</table>'
        # pre_line = '</table>'
        text = dictfile.read()
        text = re.sub('</table>', new_line, text)
        dictfile.seek(0)
        dictfile.write(text)
        dictfile.truncate()


def update_row_table(line, target_name, prev_line, new=False):
    '''
    this function update the html table by finding the closing table tag.
    then replace it with updated data.
    '''
    with open(os.path.join(__location__, target_name+'.html'), 'r+',
              encoding="utf-8") as dictfile:
        field_names = ['اليوم',
                       'الوقت']
        if new:
            field_names.append('محول من')
            field_names.append('اسم المسجل')
        else:
            field_names.append('دفتر')
        field_names.append('بطاقة علاج رقم')
        field_names.append('الرقم داخل الهيئة')
        field_names.append('القسم')
        field_names.append('الإسم')
        pre_line = prev_line
        new_line = ''
        for label in field_names:
            new_line += '<td>'
            new_line += str(line[label])
            new_line += '</td>'
            print(label)
            print(new_line)
        # pre_line = '</table>'
        text = dictfile.read()
        text = re.sub(pre_line, new_line, text)
        dictfile.seek(0)
        dictfile.write(text)
        dictfile.truncate()


def init_html():
    data_names = ["دفتر الجديد شخصي", "دفتر الجديد معاشات",
                  "دفتر الجديد أعباء"]
    x = datetime.now()
    day = '{}-{}-{}'.format(x.year, x.month, x.day)
    for name in data_names:
        creat_html(name, new=True)
        data = search_date_for_search(name, day)
        add_data_to_html(data, name, new=True)
        end_html(name)
        render_table(name)
    name = "دفتر التردد"
    creat_html(name)
    data = search_date_for_search(name, day)
    add_data_to_html(data, name)
    end_html(name)
    render_table(name)


def reinit_html(file_name):
    x = datetime.now()
    day = '{}-{}-{}'.format(x.year, x.month, x.day)
    if file_name != "دفتر التردد":
        creat_html(file_name, new=True)
        data = search_date_for_search(file_name, day)
        add_data_to_html(data, file_name, new=True)
        end_html(file_name)
    else:
        creat_html(file_name)
        data = search_date_for_search(file_name, day)
        add_data_to_html(data, file_name, new=False)
        end_html(file_name)


def html_search(data, name, new=False):
    creat_html(name, new)
    add_data_to_html(data, name, new)
    end_html(name)
    render_table(name)
