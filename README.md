# Workbenches
Adds an organizational layer to qtile, which is one step above groups.
With this layer, different work environments can be split.

## Minimal setup

Assuming usage of default parameters, embed the functionality into your config:
```python
import workbenches as wb

groups = wb.init()
keys.extend(wb.setup_keys())
```

## Show groups according to workbench
```python
wb.groupbox = widget.GroupBox(
    visible_groups=wb.workbenches.active.groups,
    ...
)

...
bar.Bar([
    ...
    wb.groupbox,
    ...
])
```

## Advanced configurations
```python
groups = wb.init(
    # Determines the number of usable workbenches and their respective icons to be displayed using `wb.widget`.
    icons=["", "🛠"],
    # Determines the number of groups per workbench.
    group_names=list("123456789"),
)
keys.extend(wb.setup_keys(
    modifier=["mod4"],
    workbench_cycle_key="tab"
))
```

## Visualization of currently active workbench in status bar

```python
wb.widget = widget.TextBox(
    wb.workbenches.active.icon,
    ...
)

...
bar.Bar([
    ...
    wb.widget,
    ...
])
```

