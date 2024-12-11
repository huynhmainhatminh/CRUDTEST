import requests

from . import *


class SynchronizedEmoji(ProgressColumn):
    def __init__(self):
        super().__init__()
        self.emojis = cycle(["ʕ•ﻌ•ʔ", "ʕ•ᴥ<ʔ", "ʕ>ᴥ•ʔ", "ʕ>ᴥ<ʔ", "ʕ𖹭ᴥ𖹭ʔ", "ʕ♥ᴥ♥ʔ", "ʕ>ᴥ<ʔ", "ʕ>ᴥ•ʔ", "ʕ•ᴥ<ʔ"])
        self.current_emoji = next(self.emojis)
        self.last_update = 0

    def render(self, task):
        elapsed_seconds = int(task.elapsed)
        if elapsed_seconds > self.last_update:
            self.current_emoji = next(self.emojis)
            self.last_update = elapsed_seconds
        text = Text(
            f"[ {self.current_emoji} ]",
            style="bold yellow1"
        )
        text.stylize("bold salmon1", 2, 3 + len(self.current_emoji))
        return text


class SynchronizedPerformance(ProgressColumn):
    def __init__(self):
        super().__init__()
        self.last_update = 3

        self.overall_progress = Progress(
            TextColumn("[progress.description]{task.description}"),
            SpinnerColumn(),
            BarColumn(style="bold spring_green2"),
            MofNCompleteColumn(),
            TimeRemainingColumn(),
            TextColumn("[progress.percentage][bold sky_blue1]{task.percentage:>3.0f}%"),
        )
        self.overall_task = self.overall_progress.add_task(
            "", vertical="top"
        )

        self.max_cpu_freq = psutil.cpu_freq().max / 1000
        self.count_cpu = psutil.cpu_count(logical=True)

        self.none_progress = Progress("{task.description}", TextColumn(""))
        self.none_progress.add_task(
            "",
        )
        self.memory_progress = Progress(
            "{task.description}",
            BarColumn(style="bold spring_green2"),
            TextColumn("[progress.percentage][bold violet]{task.percentage:>3.0f}%"),
        )
        self.memory_progress.add_task(
            "[bold yellow1][ [bold sky_blue1]MEMORY [bold yellow1]]", total=100,
            vertical="top"
        )

        self.cpu_progress = Progress(
            "{task.description}",
            BarColumn(style="bold spring_green2"),
            TextColumn("[progress.percentage][bold violet]{task.percentage:>3.0f}%"),
        )
        self.cpu_progress.add_task(
            "[bold yellow1][ [bold sky_blue1]CPU [bold yellow1]]", total=100,
            vertical="top"
        )

        self.battery_progress = Progress(
            "{task.description}",
            BarColumn(style="bold spring_green2"),
            TextColumn("[progress.percentage][bold violet]{task.percentage:>3.0f}%"),
        )
        self.battery_progress.add_task(
            "[bold yellow1][ [bold sky_blue1]BATTERY [bold yellow1]]", total=100,
            vertical="top"
        )

        self.ram_free_progress = Progress(
            "{task.description}",
            BarColumn(style="bold spring_green2"),
            TextColumn("[progress.percentage][bold violet]{task.percentage:>3.0f}%"),
        )
        self.ram_free_progress.add_task(
            "[bold yellow1][ [bold sky_blue1]RAM FREE [bold yellow1]]", total=100,
            vertical="top"
        )

        self.performance_table = Table.grid(expand=True)
        self.performance_table.add_row(
            Panel(
                Group(
                    self.memory_progress, self.none_progress, self.cpu_progress, self.none_progress,
                    self.ram_free_progress, self.none_progress, self.battery_progress
                    ),
                border_style="bold medium_spring_green",
                padding=(1, 1),
                title=f"[bold yellow1][ [bold sky_blue1]PERFORMANCE [bold yellow1]]"
            )
        )

    def render(self, task):
        elapsed_seconds = int(task.elapsed)
        if elapsed_seconds > self.last_update:
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            composite_metric = round((memory_percent * self.count_cpu) / 100, 2)
            battery = psutil.sensors_battery()

            battery_percent = battery.percent

            free_percent = (memory.free / memory.total) * 100

            self.memory_progress.update(self.overall_task, completed=memory_percent)
            self.cpu_progress.update(self.overall_task, completed=composite_metric)

            self.battery_progress.update(self.overall_task, completed=battery_percent)
            self.ram_free_progress.update(self.overall_task, completed=free_percent)

        return self.performance_table


class HeaderTitle:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            f"[bold salmon1]TOOL REG CLONE FACEBOOK [bold yellow1]( [bold sky_blue2]LDPlayer [bold bright_red]& [bold sky_blue2]Selenium[bold yellow1] )     [bold medium_spring_green]|",
            f"[bold magenta1]{datetime.now().ctime()}",
        )
        return Panel(grid, border_style="bold medium_spring_green")


class HeaderName:
    def __init__(self, name: str):
        self.name = name.split(":")

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        if "Huỳnh Mai Nhật Minh" in str(self.name[1]):
            grid.add_row(
                f"[bold dark_olive_green2] Copyright by [bold bright_white]: [bold cyan]Huỳnh Mai Nhật Minh [bold yellow1]([bold bright_red] 2005 [bold yellow1])",
            )
        else:
            grid.add_row(
                f"[bold yellow1][[bold light_slate_blue] {self.name[0]}[bold yellow1]] [bold bright_white]: [bold cyan]{self.name[1]}"
            )
        return Panel(grid, border_style="bold medium_spring_green")


class HeaderNotification:
    def __init__(self, text="Chào mừng bạn đã quay trở lại. Chúc bạn một ngày tốt lành !"):
        self.text = text

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True, padding=1)
        grid.add_column(justify="left", ratio=1)

        grid.add_row(
            f"[bold hot_pink]{self.text}"
        )

        return Panel(
            grid,
            border_style="bold medium_spring_green", padding=(1, 2),
            title=f"[bold yellow1][ [bold sky_blue1]NOTIFICATION [bold yellow1]]"
        )


class HeaderScreen:
    def __init__(self, screen=False):
        self.screen = screen

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True, padding=1)
        grid.add_column(justify="center", ratio=1)

        if self.screen:
            grid.add_row(
                f"[bold dark_olive_green2][[bold light_slate_blue] lock screen [bold dark_olive_green2]]"
            )
        else:
            grid.add_row(
                f"[bold dark_olive_green2]([bold light_slate_blue] opened screen [bold dark_olive_green2])"
            )
        return Panel(
            grid,
            border_style="bold medium_spring_green", padding=(1, 2),
            title=f"[bold yellow1][ [bold sky_blue1]SCREEN F12 [bold yellow1]]"
        )


class ProgressNone:

    def __init__(self, style):
        self.style = style

    def __rich__(self) -> Panel:
        progress_none = Progress(BarColumn(style=self.style))
        progress_none.add_task("", total=None)
        panel_progress_none = Panel(
            progress_none,
            border_style="bold medium_spring_green",
            padding=(1, 1),
        )
        return panel_progress_none


class Home:
    def __init__(self) -> None:
        self.option_to_function = {
            "func22": "[bold yellow1][[bold sky_blue1] START [bold yellow1]]",
            "func23": "[bold yellow1][[bold sky_blue1] SETTING [bold yellow1]]",
            "func26": "[bold yellow1][[bold sky_blue1] EXPORT FILE [bold yellow1]]",
            "func30": "[bold yellow1]<",
            "func31": "[bold yellow1]>",
        }
        self.layout: Layout = self.make_layout_home()

    @classmethod
    def make_layout_home(cls) -> Layout:
        layout = Layout(name="root")

        layout.split_column(
            Layout(name="main", ratio=1),
            Layout(name="footer", size=5),
        )
        layout["main"].split_column(
            Layout(name="func1", ratio=1),
            Layout(name="func2", size=49),
        )
        layout["main"]["func2"].split_row(
            Layout(name="func3", ratio=1),
            Layout(name="func4", size=50),
        )
        layout["main"]["func4"].split_column(
            Layout(name="func5", ratio=1),
            Layout(name="func6", size=26),
        )
        layout["main"]["func5"].split_column(
            Layout(name="func7", ratio=1),
            Layout(name="func8", size=14),
        )
        layout["main"]["func7"].split_column(
            Layout(name="func9", size=3),
            Layout(name="func10"),
        )
        layout["main"]["func8"].split_row(
            Layout(name="func11"),
            Layout(name="func12"),
        )
        layout["main"]["func6"].split_column(
            Layout(name="func13"),
            Layout(name="func14", size=15),
        )
        layout["main"]["func11"].split_column(
            Layout(name="func15"),
            Layout(name="func16"),
        )
        layout["main"]["func1"].split_row(
            Layout(name="func17", size=48),
            Layout(name="func18", size=85),
            Layout(name="func19"),
            Layout(name="func20", size=31),
            Layout(name="func21", size=11),
        )
        layout["main"]["func9"].split_row(
            Layout(name="func22"),
            Layout(name="func23"),
        )
        layout["main"]["func10"].split_row(
            Layout(name="func24", ratio=1),
            Layout(name="func25"),
        )
        layout["main"]["func24"].split_column(
            Layout(name="func26", ratio=1),
            Layout(name="func27", size=3),
        )
        layout["main"]["func25"].split_column(
            Layout(name="func28", ratio=1),
            Layout(name="func29", size=3),
        )
        layout["main"]["func28"].split_row(
            Layout(name="func30"),
            Layout(name="func31"),
        )
        layout["main"]["func12"].split_column(
            Layout(name="func32", size=3),
            Layout(name="func33"),
        )
        layout["main"]["func14"].split_row(
            Layout(name="func34"),
            Layout(name="func35"),
        )
        layout["footer"].split_row(
            Layout(name="footer1", size=44),
            Layout(name="footer2"),
            Layout(name="footer3", size=44),
            Layout(name="footer5", size=25),
            Layout(name="footer6", size=25),
        )
        return layout

    @classmethod
    def update_frame(cls, title_func: str) -> Panel:
        sponsor_message = Table.grid(padding=0)
        sponsor_message.add_column(style="green", justify="center")
        sponsor_message.add_row(title_func)

        additional_message = ""
        style = "bold medium_spring_green"

        if additional_message:
            sponsor_message.add_row(additional_message)

        message_panel = Panel(
            Align.center(sponsor_message, vertical="top"),
            box=box.ROUNDED,
            padding=0,
            style=style
        )
        return message_panel

    @staticmethod
    def update_type_live_die(live=0, die=0) -> Panel:
        sponsor_message = Table.grid(padding=1)
        sponsor_message.add_column(style="green", justify="left")
        sponsor_message.add_column(no_wrap=False)
        sponsor_message.add_row(
            "[bold yellow1][[bold spring_green2] LIVE [bold yellow1]][bold turquoise2] :", f'[bold violet]{live}'
        )
        sponsor_message.add_row(
            "[bold yellow1][[bold deep_pink2] DIE [bold yellow1]][bold turquoise2] :", f'[bold violet]{die}'
        )

        message = Table.grid(padding=0)
        message.add_column()
        message.add_column(no_wrap=False)
        message.add_row(sponsor_message)

        message_panel = Panel(
            Align.left(sponsor_message, vertical="top", ),
            box=box.ROUNDED,
            padding=(1, 2),
            border_style="bold medium_spring_green",
            title=f"[bold yellow1][ [bold sky_blue1]STATUS [bold yellow1]]"
        )
        return message_panel

    @staticmethod
    def update_type_fb(veri=0, noveri=0) -> Panel:
        sponsor_message = Table.grid(padding=1)
        sponsor_message.add_column(style="green", justify="left")
        sponsor_message.add_column(no_wrap=False)
        sponsor_message.add_row(
            "[bold yellow1][[bold spring_green1] VERI [bold yellow1]][bold turquoise2] :", f'[bold violet]{veri}'
        )
        sponsor_message.add_row(
            "[bold yellow1][[bold dodger_blue1] NOVERI [bold yellow1]][bold turquoise2] :", f'[bold violet]{noveri}'
        )

        message = Table.grid(padding=0)
        message.add_column()
        message.add_column(no_wrap=False)
        message.add_row(sponsor_message)

        message_panel = Panel(
            Align.left(sponsor_message, vertical="top", ),
            box=box.ROUNDED,
            padding=(1, 2),
            border_style="bold medium_spring_green",
            title=f"[bold yellow1][ [bold sky_blue1]TYPE [bold yellow1]]"
        )
        return message_panel

    @staticmethod
    def update_table(list_value="", old_count=1, last_count=23) -> Panel:
        table = Table(show_lines=True, box=box.ROUNDED)

        table.add_column("Index", justify="center", style="cyan1", no_wrap=True)
        table.add_column("UID", justify="center", style="magenta")
        table.add_column("Name", justify="center", style="magenta")
        table.add_column("Birthday", justify="center", style="green")
        table.add_column("Gender", justify="center", style="green")
        table.add_column("Password", justify="center", style="green")
        table.add_column("Email", justify="center", style="green")
        table.add_column("Type", justify="center", style="green")
        table.add_column("Status", justify="center", style="green")
        table.add_column("Time", justify="center", style="green")

        if not any(list_value):
            for _ in range(old_count, last_count):
                table.add_row(f"{_}")
        else:
            for _ in list_value:
                value = _.split("|")
                if value[8] == "DIE":
                    if value[4] == "Male":
                        table.add_row(f'[bold cyan1]{value[0]}', f'[bold yellow1]{value[1]}',
                                      f'[bold light_steel_blue]{value[2]}', f'[bold plum3]{value[3]}',
                                      f'[bold turquoise2]{value[4]}',
                                      f'[bold aquamarine1]{value[5]}',
                                      f'[bold yellow2]{value[6]}',
                                      f'[bold dodger_blue1]{value[7]}',
                                      f'[bold red1]{value[8]}', f'[bold medium_purple2]{value[9]}')
                    else:
                        table.add_row(
                            f'[bold cyan1]{value[0]}', f'[bold yellow1]{value[1]}',
                            f'[bold light_steel_blue]{value[2]}', f'[bold plum3]{value[3]}',
                            f'[bold hot_pink]{value[4]}', f'[bold aquamarine1]{value[5]}',
                            f'[bold yellow2]{value[6]}',
                            f'[bold dodger_blue1]{value[7]}',
                            f'[bold red1]{value[8]}', f'[bold medium_purple2]{value[9]}'
                            )
                else:
                    if value[4] == "Male":
                        table.add_row(
                            f'[bold cyan1]{value[0]}', f'[bold yellow1]{value[1]}',
                            f'[bold light_steel_blue]{value[2]}', f'[bold plum3]{value[3]}',
                            f'[bold turquoise2]{value[4]}',
                            f'[bold aquamarine1]{value[5]}',
                            f'[bold yellow2]{value[6]}',
                            f'[bold dodger_blue1]{value[7]}',
                            f'[bold green1]{value[8]}', f'[bold medium_purple2]{value[9]}'
                            )
                    else:
                        table.add_row(
                            f'[bold cyan1]{value[0]}', f'[bold yellow1]{value[1]}',
                            f'[bold light_steel_blue]{value[2]}', f'[bold plum3]{value[3]}',
                            f'[bold hot_pink]{value[4]}',
                            f'[bold aquamarine1]{value[5]}',
                            f'[bold yellow2]{value[6]}',
                            f'[bold dodger_blue1]{value[7]}',
                            f'[bold green1]{value[8]}',
                            f'[bold medium_purple2]{value[9]}'
                        )
            for _ in range(old_count, last_count):
                table.add_row(f"{_}")

        message = Table.grid(padding=0)
        message.add_column()
        message.add_column(no_wrap=False)
        message.add_row(table)

        message_panel = Panel(
            Align.left(table, vertical="top"),
            box=box.ROUNDED,
            padding=0,
            border_style="bold medium_spring_green",
        )
        return message_panel

    @staticmethod
    def update_setting_fb() -> Panel:
        sponsor_message = Table.grid(padding=1)
        sponsor_message.add_column(style="green", justify="left")
        sponsor_message.add_column(no_wrap=False)
        sponsor_message.add_row(
            "AVATAR FB :", f'NONE'
        )
        sponsor_message.add_row(
            "COVER FB : ", f'NONE'
        )

        sponsor_message.add_row(
            "2FA FB : ", f'NONE'
        )

        sponsor_message.add_row(
            "UNLOCK 282 : ", f'NONE'
        )

        sponsor_message.add_row(
            "STORY FB : ", f'NONE'
        )

        message = Table.grid(padding=0)
        message.add_column()
        message.add_column(no_wrap=False)
        message.add_row(sponsor_message)

        message_panel = Panel(
            Align.left(sponsor_message, vertical="top", ),
            box=box.ROUNDED,
            padding=(1, 2),
            border_style="bold medium_spring_green",
        )
        return message_panel

    @staticmethod
    def update_total_fb(total=0) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_row(
            f"[bold orange1]All Account [bold bright_white]: [bold yellow1]{total}"
        )
        return Panel(grid, border_style="bold dark_slate_gray2")

    @staticmethod
    def update_ipv4_fb() -> Panel:
        while True:
            try:
                ipv4 = requests.get("https://api.ipify.org/").text
                grid = Table.grid(expand=True)
                grid.add_column(justify="left", ratio=1)
                grid.add_row(
                    f"[bold orange1]IP [bold bright_white]: [bold cyan1]{ipv4}"
                )
                return Panel(grid, border_style="bold dark_slate_gray2")
            except(requests.RequestException, ):
                time.sleep(5)
                continue

    @staticmethod
    def update_pages(page_min=0, page_max=0) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_row(
            f"[bold orange1]PAGES [bold bright_white]: [bold cyan1]{page_min}[bold yellow1] / [bold red1]{page_max}"
        )
        return Panel(grid, border_style="bold dark_slate_gray2")

    @staticmethod
    def update_reg_fb(ld=False, sele=False, quantity=0, running=0) -> Panel:
        grid = Table.grid(expand=True, padding=1)
        grid.add_column(justify="left", ratio=1)
        if ld == "true":
            grid.add_row(
                f"[bold yellow1]LDPlayer [bold bright_white]: [bold dark_olive_green2]True"
            )
        else:
            grid.add_row(
                f"[bold yellow1]LDPlayer [bold bright_white]: [bold bright_red]False"
            )
        if sele == "true":
            grid.add_row(
                f"[bold light_cyan1]Selenium [bold bright_white]: [bold bright_green]True"
            )
        else:
            grid.add_row(
                f"[bold light_cyan1]Selenium [bold bright_white]: [bold bright_red]False"
            )

        grid.add_row(
            f"[bold light_slate_blue]Quantity [bold bright_white]: [bold violet]{quantity}"
        )

        grid.add_row(
            f"[bold orange1]Running [bold bright_white]: [bold violet]{running}"
        )
        return Panel(grid, border_style="bold medium_spring_green", padding=(1, 2))

    def update_layout(self) -> None:
        for option in self.option_to_function:
            self.layout[option].update(self.update_frame(self.option_to_function[option]))

    def run_display_home(self) -> Layout:
        self.update_layout()
        self.layout["func18"].update(HeaderTitle())
        self.layout["func17"].update(HeaderName("Copyright by : Huỳnh Mai Nhật Minh"))
        self.layout["func19"].update(HeaderName("Github : huynhmainhatminh"))
        self.layout["func20"].update(HeaderName("Telegram : @MarkJethro"))
        self.layout["func15"].update(self.update_type_live_die())
        self.layout["func16"].update(self.update_type_fb())
        self.layout["func3"].update(self.update_table())
        self.layout["func33"].update(self.update_reg_fb())
        self.layout["func32"].update(self.update_pages())
        self.layout["func27"].update(self.update_total_fb())
        self.layout["func29"].update(self.update_ipv4_fb())

        self.progress_performance = Progress("{task.description}", SynchronizedPerformance())
        self.progress_performance.add_task("", vertical="top")
        self.layout["func13"].update(self.progress_performance)

        self.progress_emoji = Progress(SynchronizedEmoji())
        self.progress_emoji.add_task("", vertical="top")
        self.panel_emoji = Panel(
            self.progress_emoji,
            border_style="bold medium_spring_green",
            padding=0,
        )
        self.layout["func21"].update(self.panel_emoji)

        self.time_progress = Progress("{task.description}", TimeElapsedColumn())
        self.time_progress.add_task(" [bold yellow1][ [bold light_slate_blue]TIME [bold yellow1]]", vertical="top")
        self.panel_time = Panel(
            self.time_progress,
            border_style="bold medium_spring_green",
            padding=(1, 1),
            title=f"[bold yellow1][ [bold sky_blue1]TIME PROGRESS [bold yellow1]]"
        )
        self.layout["footer6"].update(self.panel_time)

        self.layout["footer1"].update(ProgressNone("bold sky_blue1"))
        self.layout["footer3"].update(ProgressNone("bold blue_violet"))
        self.layout["footer2"].update(HeaderNotification())
        self.layout["footer5"].update(HeaderScreen())
        return self.layout
