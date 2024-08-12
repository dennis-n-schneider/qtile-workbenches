# Workbenches

## Setup

```python
pip install qt-workbench
```

Assuming usage of default parameters, embed the functionality into your config:
```python
groups = workbenches.init(
    group_names=list("123456789"),
    workbenches=[
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
    modifier="mod4",
    workbench_cycle_key="tab"
))
```

Show groups local to workbench:
```python
workbenches.gb
```
Customize by using a `widget.GroupBox` and accessing `workbenches.active.groups` in `visible_groups=`.

## Visualization of currently active workbench in statusbar

```python
workbenches.widget # Shows the respective icon.
```
Customize by using any `widget.TextBox` and `workbenches.active.icon`.

