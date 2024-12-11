import interface
import keyboard
import os
from rich.live import Live


def main():
    layout_home = interface.Home().run_display_home()
    interface.SelecteHome(layout_home, live=None).highlight_selected()
    with Live(layout_home, refresh_per_second=100, screen=True) as live:
        try:
            keyboard.on_press(interface.SelecteHome(layout_home, live).handle_key_press)
            keyboard.wait("esc")
        except(KeyboardInterrupt, ):
            pass


if __name__ == '__main__':
    main()