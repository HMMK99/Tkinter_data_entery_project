import csv
import os
from datetime import datetime
# from html_func import update_table

__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))


def only_number(char):
    return char.isdigit()


def check_file_exists(filename):
    '''
    checks if a file exists or not
    '''
    path = '../الدفاتر/' + filename
    if os.path.isfile(os.path.join(__location__, path)):
        return True
    else:
        return False


def add_as_dict(filename, line):
    '''
    add line as dictionary in the file name
    note: only the new files
    '''
    if check_file_exists(filename):
        path = '../الدفاتر/' + filename
        with open(os.path.join(__location__, path), 'a',
                  encoding="utf-8") as dictfile:
            field_names = ['الإسم',
                           'بطاقة علاج رقم',
                           'الرقم داخل الهيئة',
                           'القسم',
                           'اليوم',
                           'الوقت',
                           'محول من',
                           'اسم المسجل']
            csv_writer = csv.DictWriter(dictfile,
                                        fieldnames=field_names, delimiter=',')
            csv_writer.writerow(line)
    else:
        print('no such file')


def add_in_freq(line, datafile_name):
    '''add line to freq data file'''
    field_names = ['الإسم',
                   'بطاقة علاج رقم',
                   'الرقم داخل الهيئة',
                   'القسم',
                   'اليوم',
                   'الوقت',
                   'دفتر']
    line = list((line['الإسم'], line['بطاقة علاج رقم'],
                 line['الرقم داخل الهيئة'],
                 line['القسم'], line['اليوم'], line['الوقت'],
                 datafile_name))
    line = dict(zip(field_names, line))
    if check_file_exists('../الدفاتر/دفتر التردد'):
        with open(os.path.join(__location__, '../الدفاتر/دفتر التردد'),
                  'a', encoding="utf-8") as dictfile:

            csv_writer = csv.DictWriter(dictfile,
                                        fieldnames=field_names, delimiter=',')
            csv_writer.writerow(line)
        # update_table(line, "دفتر تردد")
    else:
        print('no such file')


def search_id_edit(filename, id):
    '''
    search for data by id, note: returning when finding the id
    note: make it so it searchs from below
    '''
    if check_file_exists(filename):
        path = '../الدفاتر/' + filename
        with open(os.path.join(__location__, path), 'r',
                  encoding="utf-8") as dictfile:
            csv_reader = list(csv.DictReader(dictfile, delimiter=','))
            x = datetime.now()
            today = '{}-{}-{}'.format(x.year, x.month, x.day)
            x = -1
            while csv_reader[x]["اليوم"] == today:
                if csv_reader[x]["بطاقة علاج رقم"] == id:
                    return csv_reader[x], str(x)
                x -= 1
            return False
    else:
        print('no such file')


def search_freq_id_edit(filename, id):
    '''
    search for freq data by id, note: returning when finding the id
    note: make it so it searchs from below
    '''
    if check_file_exists("دفتر التردد"):
        path = '../الدفاتر/' + "دفتر التردد"
        with open(os.path.join(__location__, path), 'r',
                  encoding="utf-8") as dictfile:
            csv_reader = list(csv.DictReader(dictfile, delimiter=','))
            x = datetime.now()
            today = '{}-{}-{}'.format(x.year, x.month, x.day)
            filename = filename.split(' ')[-1]
            print(filename)
            print(id)
            print(x)
            x = -1
            while csv_reader[x]["اليوم"] == today:
                if (csv_reader[x]["بطاقة علاج رقم"] == id and
                   csv_reader[x]["دفتر"] == filename):
                    print(csv_reader[x], str(x))
                    return csv_reader[x], str(x)
                x -= 1
            return False
    else:
        print('no such file')


def change_id_edit(filename, line, x):
    path = '../الدفاتر/' + filename
    with open(os.path.join(__location__, path), 'r', encoding='utf-8') as f:
        read = list(csv.DictReader(f, delimiter=','))

        # if line['بطاقة علاج رقم'] == read[x]['بطاقة علاج رقم']:
        for key in line.keys():
            if key in ['x', 'file_name']:
                continue
            read[x][key] = line[key]

    with open(os.path.join(__location__, path), 'w', encoding='utf-8') as f:
        col_names = list(line.keys())[:-2]
        write = csv.DictWriter(f, fieldnames=col_names, delimiter=',')
        cols = dict(zip(col_names, col_names))
        write.writerow(cols)
        for row in read:
            try:
                row.pop(None)
                write.writerow(row)
            except KeyError:
                write.writerow(row)


def verify_id_isnt_added_this_day(filename, id):
    if not search_id_edit(filename, id):
        return True
    else:
        return False


def delete_id(file_name, id, new):
    try:
        if new:
            index = int(search_id_edit(file_name, id)[1])
            path = '../الدفاتر/' + file_name
        else:
            index = int(search_freq_id_edit(file_name, id)[1])
            path = '../الدفاتر/' + 'دفتر التردد'
    except TypeError:
        print('delete_id')
        return 0
    print(index)
    with open(os.path.join(__location__, path), 'r', encoding='utf-8') as f:
        read = list(csv.DictReader(f, delimiter=','))

    field_names = ['الإسم',
                   'بطاقة علاج رقم',
                   'الرقم داخل الهيئة',
                   'القسم',
                   'اليوم',
                   'الوقت']
    if new:
        field_names.append('محول من')
        field_names.append('اسم المسجل')
    else:
        field_names.append('دفتر')

    with open(os.path.join(__location__, path), 'w', encoding='utf-8') as f:
        write = csv.DictWriter(f, fieldnames=field_names, delimiter=',')
        cols = dict(zip(field_names, field_names))
        write.writerow(cols)
        x = 0
        row_number = len(read)
        del_index = row_number + index
        for row in read:
            if x == del_index:
                print('here')
                x += 1
                continue
            write.writerow(row)
            x += 1


def search_id_for_search(filename, id):
    '''search for data by id, note: iterate over all the file'''
    if check_file_exists(filename):
        path = '../الدفاتر/' + filename
        with open(os.path.join(__location__, path), 'r',
                  encoding="utf-8") as dictfile:
            csv_reader = csv.DictReader(dictfile, delimiter=',')
            data = []
            for line in csv_reader:
                if line["بطاقة علاج رقم"] == id:
                    data.append(line)
            return data
    else:
        print('no such file')


def search_id(filename, id):
    '''
    search for data by id, note: returning when finding the id
    note: make it so it searchs from below
    '''
    data = search_id_for_search(filename, id)
    if data:
        return data[-1]
    else:
        print('found nothing')


def search_date_for_search(filename, date):
    '''search for data by date, note: iterate over all the file'''
    if check_file_exists(filename):
        path = '../الدفاتر/' + filename
        with open(os.path.join(__location__, path), 'r',
                  encoding="utf-8") as dictfile:
            csv_reader = csv.DictReader(dictfile, delimiter=',')
            data = []
            for line in csv_reader:
                if line["اليوم"] == date:
                    data.append(line)
            return data
    else:
        print('no such file')


def verify_not_empty(line):
    '''check if any field has no value'''
    if "" in line.values():
        return True
    else:
        return False


def make_temp_file(name, line):
    '''write file and add the line you want'''
    with open(os.path.join(__location__, f'{name}_temp'),
              'w', encoding="utf-8") as dictfile:
        for key, value in line.items():
            dictfile.write(key+' '+value+'\n')


def read_temp_file(name):
    '''read data from the temporary file'''
    # write code here
    check_file_exists(f'../GUI/{name}_temp')
    with open(os.path.join(__location__, f'{name}_temp'), 'r',
              encoding="utf-8") as dictfile:
        file_data = dictfile.read().split('\n')[:-1]
        if len(file_data) == 1:
            return file_data
        data = {}
        for line in file_data:
            splitted_line = line.split(' ')
            if splitted_line[0] == 'الإسم' or splitted_line[0] == 'file_name':
                data[splitted_line[0]] = ' '.join(splitted_line[1:])
            elif splitted_line[0] in ['اسم', 'محول']:
                data[' '.join(splitted_line[:2])] = ' '.join(splitted_line[2:])
            else:
                data[' '.join(splitted_line[:-1])] = splitted_line[-1]
        return data


def delete_temp_file(name):
    os.remove(os.path.join(__location__, f'{name}_temp'))
