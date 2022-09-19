# ReactComponentCreator
Консольная утилита предназначенная для автоматизации создания React компонентов.

```bash
$ rcc Component1 Component2 Component3
```
![File Component](https://github.com/init63/ReactComponentCreator/blob/main/.github/file.jpg?raw=true)

```bash
$ rcc -f --css Component1 Component2 Component3
```
![Folder Component](https://github.com/init63/ReactComponentCreator/blob/main/.github/folder.jpg?raw=true)

## Зависимости
Поддерживается Python версии 3.10+.
> **Примечание:**\
Работоспособность на меньших версиях Python не гарантируется.

## Установка
### Linux
```bash
$ git clone https://github.com/init63/ReactComponentCreator.git && cd ReactComponentCreator
```
```bash
$ chmod +x rcc
```
```bash
$ sudo ln -s $(pwd)/rcc /usr/local/bin/
```

## Параметры

Параметр | Описание | По умолчанию
---|---|---
 `-f`, `--folder` | Создать компонент тип "папка" | Создает компонент типа "файл"
 `--tsx` | Указывает на создание Typescript компонента: `NameComponent.tsx`| Указывает на создание стандартного React компонента `NameComponent.jsx`
 `-t`, `--tab-width` | Длинна табуляции в пробелах | `2`
 `semi, --no-semi` | Использовать точку с запятой `;` в конце строки | `True`
 `-s`, `--single-quote` | Использовать одинарные кавычки `'` | `False`
 `-m`, `--module` | Создать файл для модульной изоляции стилей: `NameComponent.module.css` | файл стилей не создается
 `--css , --scss , --sass , --less` | Расширение файла стилей | `*.css`
