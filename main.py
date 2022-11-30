from chbot import *
from vk_api.longpoll import VkLongPoll, VkEventType
from database import *
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


for event in bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = str(event.user_id)
        keyboard = VkKeyboard()
        keyboard.add_button('Начать поиск', VkKeyboardColor.PRIMARY)
        bot.send_but(event.user_id, f'Привет, {user_vk.get_name(event.user_id)}, для поиска нажмите: Начать поиск', keyboard)
        for event in bot.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.text == "Начать поиск":
                    users_vk_id = user_vk.search_user(user_id)
                    create_table_users()
                    for user_vk_id in users_vk_id:
                        if not select_of_table(user_id, user_vk_id):
                            user_vk_link = 'vk.com/id' + str(user_vk_id)
                            user_photos = user_vk.get_photo(user_vk_id,user_id)
                            bot.send_msg(user_id, user_vk_link)
                            add_in_table(user_id, user_vk_id)
                            try:
                                for i in user_photos:
                                    bot.send_photo(user_id, user_vk_id, i[0])
                                keyboard = VkKeyboard()
                                keyboard.add_button('Далее', VkKeyboardColor.POSITIVE)
                                bot.send_but(event.user_id,
                                             f'Чтобы получить новую анкету, нажмите: Далее',
                                             keyboard)
                            except Exception:
                                break
                            for event in bot.longpoll.listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                    request = event.text
                                    if request == 'Далее':
                                        break
                        else:
                            continue
