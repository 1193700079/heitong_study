import tracemalloc

import linecache


def display_top(snapshot, key_type="lineno", limit=100):
    # top_stats = snapshot2.compare_to(snapshot1, key_type)
    snapshot = snapshot.filter_traces(
        (
            # tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
            # tracemalloc.Filter(False, "<frozen importlib._bootstrap_external>"),
            # tracemalloc.Filter(False, "/root/anaconda3/*"),
            # tracemalloc.Filter(False, "*"), # 表明全都不接受
            tracemalloc.Filter(True, "/mnt/g/action_code/mind/main*"),  # 表明接受这个
            tracemalloc.Filter(True, "/mnt/g/action_code/mind/core*"),
            # tracemalloc.Filter(True, "/mnt/g/action_code/mind/*"),
            # tracemalloc.Filter(False, "<unknown>"),
            # tracemalloc.Filter(False, "<string>"),
            # tracemalloc.Filter(False, str(Path(__file__).parent.parent / "src" / "*")),
        )
    )

    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print(
            "#%s: %s:%s: %.1f KiB"
            % (index, frame.filename, frame.lineno, stat.size / 1024)
        )
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print("    %s" % line)

    # other = top_stats[limit:]
    # if other:
    #     size = sum(stat.size for stat in other)
    #     print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))
