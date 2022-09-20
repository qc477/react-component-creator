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
1. Скачать архив с последней версией ReactComponentCreator из раздела [релизы](https://github.com/init63/ReactComponentCreator/releases).
2. Распаковать в удобную для Вас директорию.
3. Сделать файл `rcc` исполняемым:
```bash
$ chmod +x rcc
```
4. Создать символическую ссылку на исполняемый файл `rcc` в каталог `/usr/local/bin/`:
```bash
$ sudo ln -s $(pwd)/rcc /usr/local/bin/
```
5. Можно приступать к работе.

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
