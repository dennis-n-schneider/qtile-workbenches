from libqtile.config import Group, Key
from libqtile.lazy import lazy
from libqtile import widget


class Workbench:

    def __init__(self, name, icon, groups: list):
        self.name = name
        self.icon = icon
        self._groups = groups
        self._active_group = groups[0]

    @property
    def groups(self) -> list:
        return [self.name + "_" + g for g in self._groups]

    @property
    def active_group(self):
        return self._active_group

    @active_group.setter
    def active_group(self, group_id: int):
        self._active_group = self.groups[group_id]
    

class WorkbenchManager:

    def __init__(self, workbenches=None):
        if workbenches is None:
            self._workbenches = []
        else:
            self._workbenches = workbenches
        self._active = 0

    def __iter__(self):
        return iter(self._workbenches)

    @property
    def active(self):
        return self._workbenches[self._active]

    @active.setter
    def active(self, active_id: int):
        self._active = active_id

    def cycle(self, amount=1):
        self._active = (self._active+amount)%len(self._workbenches)

    # TODO Register any GroupBox and TextBox!


mod = "mod4"
bar_color = "#222255"

group_names = "123456789"

workbenches = WorkbenchManager([
    Workbench("", "", list(group_names)),
    Workbench("work", "🛠", list(group_names)),
])

@lazy.screen.function
def cycle_workbenches(s):
    global _currently_visible_workbench 
    # Cycle currently visible workbench.
    workbenches.cycle()
    s.toggle_group(workbenches.active.active_group)
    gb.visible_groups=workbenches.active.groups
    workbench_widget.update(workbenches.active.icon)

@lazy.screen.function
def go_to_screen(s, i):
    workbenches.active.active_group = i
    s.toggle_group(workbenches.active.active_group)

@lazy.window.function
def move_to_screen(w, i):
    w.togroup(workbenches.active.groups[i])

def setup_workbenches_groups():
    groups = [Group(g, label="󰝥")
        for wb in workbenches
        for g in wb.groups]
    return groups

def setup_workbenches_keys(modifiers=None, key="escape"):
    if modifiers is None:
        modifiers = ["mod4"]
    """Initialize keys to the workbench workflow.
    Cycling between both screens and workbenches.

    Parameters
    ----------
    modifiers : list[str]
        A list of modifiers, usually the default modifier mod.
    key : str
        The key to trigger the workbench-cycling.

    Returns
    -------
    list[Key]
        The keys needed to cycle between both screens and workbenchs.
    """
    keys = [
        Key(modifiers, key, cycle_workbenches(), desc="Cycle workbench")
    ]
    for i, group_name in enumerate(group_names):
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    group_name,
                    go_to_screen(i),
                    desc="Switch to group {}".format(group_name),
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    group_name,
                    move_to_screen(i),
                    desc="Move focused window to group {}".format(group_name),
                ),
            ]
        )
    return keys

workbench_widget = widget.TextBox(workbenches.active.icon,
                    foreground="#7777BB",
                    background=bar_color, 
                    padding=0,
                    fontshadow=bar_color,
                    fontsize=16)

gb = widget.GroupBox(highlight_method="text",
                     visible_groups=workbenches.active.groups,
                     center_aligned=True,
                     this_current_screen_border="#EEEEFF",
                     active="#7777BB",
                     background="#000000.0",
                     fontsize=12,
                     )


