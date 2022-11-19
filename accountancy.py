documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': ['111']
}


def show_name_by_doc(doc_list, dir):
    doc_num = input('Введите номер документа: ')
    res = []
    for document in doc_list:
        res = [*res, *list(document.values())]
    while doc_num not in res:
        if doc_num == 'Q':
            return('Возврат в меню.')
            break
        return('Документ не найден, введите номер документа: ')
    for document in doc_list:
        if doc_num in document.values():
            return(document['name'])


def show_shelf_by_doc(doc_list, dir):
    doc_num = input('Введите номер документа: ')
    res = []
    for i in list(directories.values()):
        res = [*res, *i]
    while doc_num not in res:
        if doc_num == 'Q':
            return('Возврат в меню.')
            break
        else:
            return('Документ не найден, введите номер документа: ')

    for shelf, docs in dir.items():
        if doc_num in docs:
            return(f'Он на полке {shelf}')


def all_documents(doc_list, dir):
    all = []
    for document in doc_list:
        all.append(f'{list(document.values())[0]} "{list(document.values())[1]}" "{list(document.values())[2]}"')
    return all

def add_new_doc(doc_list, dir):
    keys = ['type', 'number', 'name']
    value = [input('Введите тип документа: '), input('Введите номер документа: '), input('Введите имя: ')]
    new_user = dict(zip(keys, value))
    shelf = input('На какую полку поместить? ')
    while shelf not in directories.keys():
        shelf = input('Выберите существующую полку: ')
        if shelf == 'Q':
            print('Возврат в меню.')
            break
    else:
        doc_list.append(new_user)
        dir[shelf].append(value[1])
        print(f'Успешно помещено на полку {shelf}')
    return (doc_list, dir)


def delete_doc(doc_list, dir):
    doc_num = input('Введите номер документа: ')
    res = []
    for i in list(dir.values()):
        res = [*res, *i]
    while doc_num not in res:
        doc_num = input('Документ не найден на полке, введите номер документа: ')
        if doc_num == 'Q':
            print('Возврат в меню.')
            break
    for document in doc_list:
        if doc_num in document.values():
            doc_list.remove(document)
    for shelf, docs in dir.items():
        if doc_num in docs:
            docs.remove(doc_num)
            print('Удалено')


def move_doc(doc_list,
             dir):  # Получилось, что функция работает вне зависимости от того, вводят номер старой полки или нет.
    doc_num = input('Введите номер документа: ')
    res = []
    for i in list(dir.values()):
        res = [*res, *i]
    while doc_num not in res:
        doc_num = input('Документ не найден, введите номер документа: ')
        if doc_num == 'Q':
            print('Возврат в меню.')
            break
    else:
        old_shelf, new_shelf = input('Введите номер полки: '), input('Переместить на полку: ')
        while new_shelf not in dir.keys():
            new_shelf = input('Выберите существующую полку: ')
            if new_shelf == 'Q':
                print('Возврат в меню.')
                break
        else:
            for shelf, docs in dir.items():
                if doc_num in docs:
                    docs.remove(doc_num)
            dir[new_shelf].append(doc_num)
            print(f'Перемещено на полку {new_shelf}')

    return (dir)


def add_new_shelf(doc_list, dir):
    new_shelf = input('Введите номер новой полки: ')
    while new_shelf in dir.keys():
        new_shelf = input('Такая полка уже есть, введите другой номер: ')
        if new_shelf == 'Q':
            print('Возврат в меню.')
            break
    else:
        dir.setdefault(new_shelf, [])


def main(doc_list, dir):
    print(
        'Список команд: \np – people: команда, которая спросит номер документа и выведет имя человека, которому он принадлежит; \ns – shelf: команда, которая спросит номер документа и выведет номер полки, на которой он находится. \nl– list: команда, которая выведет список всех документов \na – add: команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. \nd – delete: команда, которая спросит номер документа и удалит его из каталога и из перечня полок. \nm – move: команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.\nas – add shelf: команда, которая спросит номер новой полки и добавит ее в перечень.\nQ: выйти в главное меню или вообще =).')
    print()
    inputDict = {'p': show_name_by_doc, 's': show_shelf_by_doc, 'l': all_documents, 'a': add_new_doc, 'd': delete_doc,
                 'm': move_doc, 'as': add_new_shelf}
    while True:
        command = input('Введите команду: ')
        if command == 'Q':
            print('Ну всё, конец.')
            break
        inputDict[command](doc_list, dir)


all_documents(documents, directories)
