# coding:utf-8
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand
from app.main import create_app, db
from app.todo.models import USER, TODO

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def init_db():
    return dict(app=app, db=db, User=USER, Todo=TODO)


manager.add_command("shell", Shell(make_context=init_db))
manager.add_command("db", MigrateCommand)
manager.add_command('runserver',
                    Server(host='0.0.0.0',
                           port=9000,
                           use_debugger=True))


if __name__ == '__main__':
    manager.run()