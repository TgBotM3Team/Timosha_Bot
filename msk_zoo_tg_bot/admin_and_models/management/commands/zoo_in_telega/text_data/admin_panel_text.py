HELLO_ADMIN = """
Вы являетесь администратором этого бота и имеете доступ к его скрытому функционалу!
Если Вам нужна помощь, нажмите кнопку <b><i>help</i></b> 👇🏻
"""


NOT_ADMIN = """
Прости, но мне не сказали, что ты админ☹️
Я не могу открыть тебе доступ...
"""


HELP_ADMIN = """
Для того, чтобы получить id файла, <b>просто отправьте его в чат</b>

<i>Напоминаем, что:</i>

✅Если Тимофей отправляет большую картинку (как в выводе результата после прохождения викторины), это фото, отправленное <b>С СЖАТИЕМ</b>

✅Если Тимофей отправляет картинку файлом (как при нажатии кнопки "Сохранить результат") это фото, отправленное <b>БЕЗ СЖАТИЯ</b>. Это сохраняет качество изображения на высоком уровне!

Это два разных типа файлов, вид их id отличается, будьте внимательны!

После получения id, скопируйте его, зайдите в администраторскую панель Django и добавьте в соответствующее поле.
<b>Не забудьте сохранить!</b>

P.S. id одинаковы при каждом отправлении только в этом боте и не могут быть использованы в других чатах.
Если Вы случайно очистите историю чата, при повторном отправлении файлов, их id не изменятся!

Для того, чтобы выйти из панели администратора, нажмите кнопку 'stop'
"""


ADMIN_STATE_ALREADY_TEXT = """
Вы уже находитесь в панели администратора.
"""


CANCELLED_FEEDBACK_ACTIVATED_ADMIN_STATE_TEXT = """
Вы отменили создание отзыва и активировали панель администратора.
"""


CANCELLED_QUIZ_ACTIVATED_ADMIN_STATE_TEXT = """
Вы отменили опрос и активировали панель администратора.
"""


NOT_IN_ADMIN_STATE = """
Вы не активировали панель администратора.
Сделайте это с помощью меню, чтобы воспользоваться её функциями.
"""


QUIT_ADMIN_PANEL_TEXT = """
Вы вышли из панели администратора.
"""
