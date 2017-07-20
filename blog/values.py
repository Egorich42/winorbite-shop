import vk
token = 'https://oauth.vk.com/blank.html#access_token=428d4056e19bbcb3045aa198eaf5efc0b8ce3b68ae4e2405a81dd177a23df83fc40052d7623d8e45d0c9e&expires_in=0&user_id=31383913'
session = vk.AuthSession('6049127', 'zonaegora@mail.ru', 'elonbatya42r',  scope='wall, messages')
vk_api = vk.API(session)