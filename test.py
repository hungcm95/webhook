from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='PythonSampleBot',
	avatar='http://viber.com/avatar.jpg',
	auth_token='51913fbfd8329634-859b75f412762a17-b032688d1faf99e1'
)
viber = Api(bot_configuration)

print(viber)