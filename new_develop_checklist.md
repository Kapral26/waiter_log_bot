Это схема Чек листа, но YT имеет траблы с его заполнением, в связи с этим файл для OneNote во вложении.

*Наставник:* --Указываем ФИО наставника
*Стажер:* --Указываем ФИО стажера



| Цели на прохождение испытательного срока | Ожидаемый результат |
| --- | --- |
| Погружение в разработку\\доработку\\развитие проекта ИС КРР(Информационной системы Контроля Ревизионной Работы) | Активное вовлечение в разработку\\доработку\\развитие проекта ИС КРР |
| Погружение в специфику работы разработку\\доработку\\развитие проекта ИС КРР | Самостоятельное выполнение задач направленное на разработку\\доработку\\развитие проекта ИС КРР |
| Прохождение адаптационного чек-листа | на 100% выполненный чек-лист |



# Чек листы по временным промежуткам:

## Первая неделя работы ***(Дата окончания)***

* [ ] Занять рабочее место
* [ ] Настроить почту, добавить подпись
* [ ] Настроить Teams
* [ ] Получить доступ к YouTrack(<https://v00youtrack.corp.tander.ru/>)
* [ ] Ознакомиться с [Вводной информацией ]()
* [ ] Получить пропуск в офис
* [ ] Установить\\убедиться, что установлен необходимый софт
  * [ ] GitBash
  * [ ] Pycharm
  * [ ] Notepad++
  * [ ] Oracle Client
  * [ ] Putty
  * [ ] Python 2.7.17
  * [ ] Python 3.8.6
  * [ ] Winscp
  * [ ] Dbeawer
  * [ ] Ibexpert - в каталоге c ПО обязательно должен быть файлы("fbclient.dll", "gds32.dll") - в закрепе.
  * [ ] Конфигуратор справочников - наше ПО, ставим самостоятельно.
  * [ ] OracleDeveloper
  * [ ] SQL Server manager studio
* [ ] Убедиться, что есть все необходимые доступы
  * [ ] К боевой ИС(<https://rao.corp.tander.ru/>)
  * [ ] К тестовой ИС([https://test.rao.corp.tander.ru/](https://test.rao.corp.tander.ru:86/))
  * [ ] В YouTrack проекта портал РЮБ(<https://v00youtrack.corp.tander.ru/>)
  * [ ] В GitLab(<https://coderepo.corp.tander.ru/>)
  * [ ] В Confluence(<https://spaces.corp.tander.ru/pages/viewpage.action?pageId=1006688562>)
* [ ] Получить необходимые пароли для работы @hmelnickiy_ss
* [ ] Подтвердить наличие необходимых сетевых доступов @hmelnickiy_ss
* [ ] Настроить удалённое подключение [https://magnit-info.ru/rem/](https://magnit-info.ru/rem/ "https://magnit-info.ru/rem/")
* [ ] Пройти курсы:
  * [ ] [Письменные коммуникации](https://magnum.magnit.ru/view_doc.html?mode=course&object_id=6281536963414330309)
  * [ ] [Работа с программой MS Outlook](https://magnum.magnit.ru/view_doc.html?mode=course&object_id=6782529454398047736)

## Вторая неделя работы ***(Дата окончания)***

* [ ] Настроить подключения к БД
  * [ ] Firebird - "Ibexpert"
    * [ ] master
    * [ ] test
    * [ ] dev
  * [ ] Postgresql - "Dbeaver"
    * [ ] master
    * [ ] test
    * [ ] dev
  * [ ] Oracle - "SQLDeveloper"
    * [ ] БДСМ тест
    * [ ] Один из РЦ
  * [ ] MSSQL
    * [ ] Настройка ODBC
    * [ ] Все hyper
  * [ ] БД ENS сервера
* [ ] Настроить работу "Конфигуратора справочников"
* [ ] Настроить Pycharm
* [ ] Запустить локальную версию портала
* [ ] Ознакомиться с организационно-техническим решением портала РЮБ, [ссылка](https://it-portal.corp.tander.ru/pages/viewpage.action?pageId=1167753758)
* [ ] Ознакомиться с описанием структуры описанных структуры БД Firebird, [ссылка](https://spaces.corp.tander.ru/pages/viewpage.action?pageId=1051295846&spaceEditingRestriction=true)
* [ ] Ознакомление с описанием структуры БДСМ\\РЦ, [ссылка](https://it-portal.corp.tander.ru/pages/viewpage.action?pageId=140214420)
* [ ] Ознакомление с описанием структуры Терадаты, [ссылка](https://data.cloudmagnit:9443/data/view/id/9643#!tab-data-structure)

## Первый месяц работы ***(Дата окончания)***

* [ ] Изучение внутреннего сервиса [log.io](https://coderepo.corp.tander.ru/svc_rao/instructions/-/tree/master/Log.io)
* [ ] Изучение работы ens сервера
* [ ] Изучение модулей ens модулей
  * [ ] Основной модуль ens_settings
    * [ ] Notify
    * [ ] dates
    * [ ] Методы работы с БД
      * [ ] oracle
      * [ ] firebird
      * [ ] mssql
      * [ ] teradata
      * [ ] postgresql
    * [ ] logger
    * [ ] ThreadRequestDataRC
    * [ ] ApiServices
* [ ] Изучение возможностей API, взаимодействие через Swagger

## Второй месяц работы ***(Дата окончания)***

* [ ] Реализовать инструмент "Справочник актуальных товаров в разрезе операций", [ссылка](https://v00youtrack.corp.tander.ru/articles/RYB-A-10/%D0%A2%D0%97-%22%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA-%D0%B0%D0%BA%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2-%D0%B2-%D1%80%D0%B0%D0%B7%D1%80%D0%B5%D0%B7%D0%B5-%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B9%22)
* [ ] **!Опционально**
  * [ ] Выбрать скрипт, который уже внедрен в работу, и, по согласованию с наставником, произвести рефакторинг.

## Третий месяц работы ***(Дата окончания)***

* [ ] Пройти аттестацию

Аттестация проходит в устном формате, по примеру экзамена.

На время подготовки к аттестации, информацию можно искать самостоятельно, можно запрашивать у коллег, не являющимся Руководителем сектора и Начальника отдела.

По ходу ответов на указанные вопросы, могут возникать параллельные. Учтите это в подготовке.

По ходу ответов на указанные вопросы могут возникать параллельные. Учтите это в подготовке.

* [ ] ИС - WEB
  * [ ] Что представляет собой ИС  со стороны пользователя, какие функции выполняет.
  * [ ] Что представляет собой ИС со стороны разработки:
    * [ ] Серверная часть ИС, какие технологии
    * [ ] Какие технологии использует для функционирования
    * [ ] Основные модули, используемые в работе:
    * [ ] Авторизация
      * [ ] CRUD-Формы
      * [ ] Обработка событий полей
      * [ ] Сценарии(Wizard)
    * [ ] Рабочий стол
      * [ ] Работа с файлами
      * [ ] Фильтры
      * [ ] Ядро справочника
    * [ ] Иерархическая структура
      * [ ] Дочерние таблицы
    * [ ] Вспомогательные модули(mlib):
      * [ ] Методы для работы с контекстом
      * [ ] Методы для работы с DateTime
      * [ ] Методы для работы с Пользователем
      * [ ] Методы для работы с Файлами
      * [ ] Методы для работы с LDAP
      * [ ] Методы для работы с SQL
      * [ ] Методы для работы с HTTP
      * [ ] Методы для работы с Route
      * [ ] …
    * [ ] Что такое Конфигуратор справочника, описание работы и основных окон
    * [ ] Справочник
    * [ ] Главная форма
      * [ ] Типы полей: text ,numeric ,TextArea ,HtmlEditor ,hidden ,comboBox ,CheckBox ,ChildTable ,LookUp ,date ,datePeriod ,photo ,link ,MultipleLookUp ,MLookUpCreate ,FormField ,FileField ,LovCombo ,CheckedLookUp ,Button – кнопка.,MonthField ,
    * [ ] Права должностей\\ролей
    * [ ] Формы
    * [ ] Фильтры.
    * [ ] На основе каких БД, можно строить справочники
* [ ] ENS-Сервер
  * [ ] Что из себя представляет, для чего необходим
  * [ ] Основные модули, используемые в работе(чем больше сможете предоставить информации.  тем лучше)
  * [ ] С какими БД он имеет возможность взаимодействовать
  * [ ] Описать алгоритм отправки писем.
* [ ] БД
  * [ ] Какие СУБД используются
  * [ ] Какие особенности при работе с БД имеются
  * [ ] Как организовано хранение в БД информации необходимой для работы справочников
  * [ ] Что такое секвенции, где и для чего используются