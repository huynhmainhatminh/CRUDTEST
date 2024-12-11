import time
import psutil
import requests
import threading
import json
import re
import auto
import sys
import os
import random
import subprocess
from rich.layout import Layout
from rich.table import Table
from rich.align import Align
from rich.panel import Panel
from rich.live import Live
from rich import box
from rich.text import Text
from rich.console import Group
from rich.console import Console
from rich.progress import (
    BarColumn, Progress, SpinnerColumn, TimeRemainingColumn,
    MofNCompleteColumn, TimeElapsedColumn, TextColumn, ProgressColumn
)
from datetime import datetime
from collections import deque
from itertools import cycle
from interface.home import *
from interface.selecte_home import *

console = Console()
