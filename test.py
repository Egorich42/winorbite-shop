import vk
token = 'https://oauth.vk.com/blank.html#access_token=428d4056e19bbcb3045aa198eaf5efc0b8ce3b68ae4e2405a81dd177a23df83fc40052d7623d8e45d0c9e&expires_in=0&user_id=31383913'
session = vk.AuthSession('6049127', 'zonaegora@mail.ru', 'elonbatya42r',  scope='wall, messages')


vk_api = vk.API(session)



egor = vk_api.users.get(user_id=31383913)
glic = vk_api.users.getFollowers(user_id=31383913, count=2, fields = 'photo_50')
groups = vk_api.users.getSubscriptions(extended=1, count=2, fields='name')
#vk_api.wall.post(users_id=0,  message="hello")
vk_api.wall.post(owner_id=-140316393,attachments='http://winorbite.com/blog/Injustice2-story/', message="Написал тут про игоры",from_group=1,signed=1)

