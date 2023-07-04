from emoji import emojize

START_MSG = emojize(':house: <b>Главное меню</b>\n\n'
                    ':exclamation: <i>Для заказа у вас должен быть установлено имя пользователя в telegram.</i>',
                    language='alias')
SELECT_CATEGORY_MSG = emojize(':memo: <b>Выберите категорию заказа:</b>', language='alias')
WRITE_TASKS_MSG = emojize(
    ':white_check_mark: <b>Вы выбрали категорию:</b> <code>{category}</code>\n\n'
    ':pencil2: <b>Введите техническое задание:</b>',
    language='alias')
WRITE_PRICE_MSG = emojize(
    ':white_check_mark: <b>Вы выбрали категорию:</b> <code>{category}</code>\n\n'
    ':pencil2: <b>Теперь введите допустимый бюджет разработки:</b>',
    language='alias')
WRITE_DEADLINE_MSG = emojize(
    ':white_check_mark: <b>Вы выбрали категорию:</b> <code>{category}</code>\n'
    '<b>Бюджет разработки:</b> <code>{price}</code>\n\n'
    ':pencil2: <b>Укажите срок выполнения:</b>',
    language='alias')
CONFIRM_ORDER_MSG = emojize(
    ':white_check_mark: <b>Вы выбрали категорию:</b> <code>{category}</code>\n'
    '<b>Техническое задание:</b> <code>{tasks}</code>\n'
    '<b>Бюджет разработки:</b> <code>{price}</code>\n'
    '<b>Срок выполнения:</b> <code>{deadline}</code>\n\n'
    ':pushpin: <b>Подтвердите данные:</b>',
    language='alias')
CONFIRMED_ORDER_MSG = emojize(':white_check_mark: <b>Заказ успешно создан, в скором времени с вами свяжутся!</b>',
                              language='alias')

CANCEL_ALERT = emojize(':x: Действие отменено!', language='alias')
NO_USERNAME_ALERT = emojize(':exclamation: У вас не установлено имя пользователя!')

# ADMIN
ADMIN_MSG = emojize(':gear: <b>Админ-панель</b>', language='alias')
SHOW_ORDERS_MSG = '<b>Заказ #</b><code>{order_id}</code>\n\n' \
                  'USER ID: <code>{user_id}</code>\n' \
                  'Категория: <code>{category}</code>\n' \
                  'ТЗ: <code>{tasks}</code>\n' \
                  'Бюджет: <code>{price}</code>\n' \
                  'Срок: <code>{deadline}</code>\n' \
                  'Контакт: <code>@{contact}</code>\n'
NEW_ORDER_MSG = emojize(':grey_exclamation: <b>Новый заказ</b>', language='alias')

NO_ORDERS_ALERT = emojize(':x: Нет заказов!', language='alias')
READ_ALERT = emojize(':grey_exclamation: Прочитано!', language='alias')
