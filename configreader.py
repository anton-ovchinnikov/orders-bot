from os import getenv


class Config:
    bot_token: str = getenv('BOT_TOKEN', 'Value is not setup!')
    admin_id: int = int(getenv('ADMIN_ID', 'Value is not setup!'))


config = Config()
