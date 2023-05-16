import time

total = 500
bar_total = 100
cnt = 0
step = 1
for i in range(total):
    cnt += step
    bar_count = (int((cnt/total) * bar_total))
    space_count = bar_total - bar_count
    time.sleep(0.02)
    print("Progress [",
        "█" * int(bar_count),
        " " * int(space_count),
        " ]",
        f'{cnt/total:.2%}',
        end = '\r',
        sep = "")
input()
