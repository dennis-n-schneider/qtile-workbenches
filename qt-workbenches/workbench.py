from libqtile import widget
from libqtile.config import Group, Key
from libqtile.lazy import lazy

from core import WorkbenchManager, Workbench


workbenches: WorkbenchManager
groupbox: widget.GroupBox
widget: widget.TextBox


def init(
    configs: list[dict[str, str]],
    group_names: list = list("123456789"),
):
    global workbenches
    workbenches = WorkbenchManager([
        Workbench(wb.get("name", ""), wb.get("icon", ""), group_names)
        for wb in configs
    ])
    groups = [Group(g, label="󰝥")
        for wb in workbenches
        for g in wb.groups]
    return groups

@lazy.screen.function
def cycle_workbenches(s):
    workbenches.cycle()
    s.toggle_group(workbenches.active.active_group)
    groupbox.visible_groups=workbenches.active.groups
    widget.update(workbenches.active.icon)

@lazy.screen.function
def go_to_screen(s, i):
    workbenches.active.active_group = i
    s.toggle_group(workbenches.active.active_group)

@lazy.window.function
def move_to_screen(w, i):
    w.togroup(workbenches.active.groups[i])

def setup_keys(modifiers=None, workbench_cycle_key="tab"):
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
        Key(modifiers, workbench_cycle_key, cycle_workbenches(), desc="Cycle workbench")
    ]
    for i, group_name in enumerate(workbenches.active.groups):
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    modifiers,
                    group_name,
                    go_to_screen(i),
                    desc="Switch to group {}".format(group_name),
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    modifiers + ["shift"],
                    group_name,
                    move_to_screen(i),
                    desc="Move focused window to group {}".format(group_name),
                ),
            ]
        )
    return keys
