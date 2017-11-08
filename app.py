from controllers.root_controller import RootController


def main():
    RootController.get_instance().start()


if __name__ == '__main__':
    main()
