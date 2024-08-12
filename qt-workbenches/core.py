class Workbench:

    def __init__(self, name, icon, groups: list):
        self.name = name
        self.icon = icon
        self._groups = groups
        self._active_group = self.groups[0]

    @property
    def groups(self) -> list:
        return [self.name + "_" + g if self.name else g
            for g in self._groups]

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

