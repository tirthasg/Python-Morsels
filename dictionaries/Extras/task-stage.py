task_runs = [
    ["stage1", 38],
    ["stage1", 47],
    ["stage1", 52],
    ["stage2", 27],
    ["stage2", 12],
    ["stage2", 23],
    ["stage3", 62],
    ["stage3", 56],
    ["stage3", 63],
]

result = {}
for task_run in task_runs:
    result.setdefault(task_run[0], []).append(task_run[1])

print(result)
