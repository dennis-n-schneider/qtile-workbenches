# Workbenches
Adds an organizational layer to qtile, which is one step over groups.
With this layer, different work environments can be split.

## Minimal setup

Assuming usage of default parameters, embed the functionality into your config:
```python
groups = workbenches.init()
keys.extend(workbenches.setup_keys())
```

## Show groups according to workbench
```python
workbenches.groupbox = widget.GroupBox(
    visible_groups=workbenches.workbenches.active.groups,
    ...
)
```

## Advanced configurations
```python
groups = workbenches.init(
    group_names=list("123456789"),
    configs=[
        {
            "name": "",
            "icon": ""
        },
        {
            "name": "work",
            "icon": "🛠"
        },
    ],
)
keys.extend(workbenches.setup_keys(
    modifier=["mod4"],
    workbench_cycle_key="tab"
))
```

## Visualization of currently active workbench in status bar

```python
workbenches.width = widget.TextBox(
    workbenches.workbenches.active.icon,
    ...
)
```

