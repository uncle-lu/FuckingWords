# coding : utf-8

from FW.app import create_app

App = create_app()

if __name__ == '__main__':
    App.run(port=80)