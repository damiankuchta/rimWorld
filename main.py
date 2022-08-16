from Colony import Colony
from GUI.GUI import GUI as G


def main():
    colony = Colony()

    gui = G(colony)
    gui.start(colony)


if __name__ == '__main__':
    main()
