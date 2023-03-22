from barony.pygame_app.application import PygameApplication


def main():
    app = PygameApplication()
    app.load_assets()
    app.run()

if __name__ == "__main__":
    main()
