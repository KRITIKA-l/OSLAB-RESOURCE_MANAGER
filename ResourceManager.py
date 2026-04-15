# ================= SMART OS RESOURCE MANAGER =================

TIME_UNIT = "ms"

# ================= SCHEDULER =================

class Scheduler:

    # ---------- FCFS (Non-Preemptive) ----------
    @staticmethod
    def fcfs(n, at, bt):
        order = sorted(range(n), key=lambda i: at[i])
        time = 0
        wt, tat, ct = [0]*n, [0]*n, [0]*n
        gantt = []

        for i in order:
            if time < at[i]:
                time = at[i]

            start = time
            time += bt[i]
            ct[i] = time

            tat[i] = ct[i] - at[i]
            wt[i] = tat[i] - bt[i]

            gantt.append((f"P{i+1}", start, time))

        return wt, tat, ct, gantt


    # ---------- SJF (Non-Preemptive) ----------
    @staticmethod
    def sjf(n, at, bt):
        completed = [False]*n
        time = 0
        wt, tat, ct = [0]*n, [0]*n, [0]*n
        gantt = []

        while False in completed:
            idx, min_bt = -1, float('inf')

            for i in range(n):
                if at[i] <= time and not completed[i] and bt[i] < min_bt:
                    idx = i
                    min_bt = bt[i]

            if idx == -1:
                time += 1
                continue

            start = time
            time += bt[idx]  # Non-Preemptive
            ct[idx] = time

            tat[idx] = ct[idx] - at[idx]
            wt[idx] = tat[idx] - bt[idx]

            gantt.append((f"P{idx+1}", start, time))
            completed[idx] = True

        return wt, tat, ct, gantt


    # ---------- SRTF (Preemptive) ----------
    @staticmethod
    def srtf(n, at, bt):
        rem = bt[:]
        time, complete = 0, 0
        wt, tat, ct = [0]*n, [0]*n, [0]*n
        gantt = []
        prev = -1

        while complete != n:
            idx, min_rem = -1, float('inf')

            for i in range(n):
                if at[i] <= time and rem[i] > 0 and rem[i] < min_rem:
                    idx = i
                    min_rem = rem[i]

            if idx == -1:
                time += 1
                continue

            if prev != idx:
                gantt.append([f"P{idx+1}", time, None])

            rem[idx] -= 1  # Preemptive
            time += 1
            gantt[-1][2] = time
            prev = idx

            if rem[idx] == 0:
                complete += 1
                ct[idx] = time
                tat[idx] = ct[idx] - at[idx]
                wt[idx] = tat[idx] - bt[idx]

        return wt, tat, ct, gantt


    # ---------- Priority (Non-Preemptive) ----------
    @staticmethod
    def priority_np(n, at, bt, pr):
        completed = [False]*n
        time = 0
        wt, tat, ct = [0]*n, [0]*n, [0]*n
        gantt = []

        while False in completed:
            idx, best = -1, -float('inf')

            for i in range(n):
                if (at[i] <= time and not completed[i] and
                    (pr[i] > best or (pr[i] == best and at[i] < at[idx]))):
                    idx = i
                    best = pr[i]

            if idx == -1:
                time += 1
                continue

            start = time
            time += bt[idx]  # Non-Preemptive
            ct[idx] = time

            tat[idx] = ct[idx] - at[idx]
            wt[idx] = tat[idx] - bt[idx]

            gantt.append((f"P{idx+1}", start, time))
            completed[idx] = True

        return wt, tat, ct, gantt


    # ---------- Priority (Preemptive) ----------
    @staticmethod
    def priority_p(n, at, bt, pr):
        rem = bt[:]
        time, complete = 0, 0
        wt, tat, ct = [0]*n, [0]*n, [0]*n
        gantt = []
        prev = -1

        while complete != n:
            idx, best = -1, -float('inf')

            for i in range(n):
                if (at[i] <= time and rem[i] > 0 and
                    (pr[i] > best or (pr[i] == best and at[i] < at[idx]))):
                    idx = i
                    best = pr[i]

            if idx == -1:
                time += 1
                continue

            if prev != idx:
                gantt.append([f"P{idx+1}", time, None])

            rem[idx] -= 1  # Preemptive
            time += 1
            gantt[-1][2] = time
            prev = idx

            if rem[idx] == 0:
                complete += 1
                ct[idx] = time
                tat[idx] = ct[idx] - at[idx]
                wt[idx] = tat[idx] - bt[idx]

        return wt, tat, ct, gantt


    # ---------- Round Robin (Preemptive) ----------
    @staticmethod
    def round_robin(n, at, bt, q):
        rem = bt[:]
        time = 0
        queue = []
        visited = [False]*n
        wt, tat, ct = [0]*n, [0]*n, [0]*n
        gantt = []

        while True:
            for i in range(n):
                if at[i] <= time and not visited[i]:
                    queue.append(i)
                    visited[i] = True

            if not queue:
                if all(rem[i] == 0 for i in range(n)):
                    break
                time += 1
                continue

            i = queue.pop(0)
            start = time

            if rem[i] > q:
                time += q
                rem[i] -= q
            else:
                time += rem[i]
                rem[i] = 0
                ct[i] = time

            gantt.append((f"P{i+1}", start, time))

            for j in range(n):
                if at[j] <= time and not visited[j]:
                    queue.append(j)
                    visited[j] = True

            if rem[i] > 0:
                queue.append(i)

        for i in range(n):
            tat[i] = ct[i] - at[i]
            wt[i] = tat[i] - bt[i]

        return wt, tat, ct, gantt


# ================= MEMORY =================

class MemoryManager:

    @staticmethod
    def fifo(pages, frames, verbose=True):
        mem, faults = [], 0
        steps = []
        if verbose:
            print("\nFIFO Execution:")
        for p in pages:
            hit = p in mem
            if p not in mem:
                faults += 1
                if len(mem) < frames:
                    mem.append(p)
                else:
                    mem.pop(0)
                    mem.append(p)
                if verbose:
                    print(f"{p} -> MISS -> {mem}")
            else:
                if verbose:
                    print(f"{p} -> HIT  -> {mem}")
            steps.append({"page": p, "hit": hit, "memory": mem[:]})
        if verbose:
            print(f"Total Page Faults: {faults}")
        return faults, steps


    @staticmethod
    def lru(pages, frames, verbose=True):
        mem, faults = [], 0
        steps = []
        if verbose:
            print("\nLRU Execution:")
        for p in pages:
            hit = p in mem
            if p not in mem:
                faults += 1
                if len(mem) < frames:
                    mem.append(p)
                else:
                    mem.pop(0)
                    mem.append(p)
                if verbose:
                    print(f"{p} -> MISS -> {mem}")
            else:
                mem.remove(p)
                mem.append(p)
                if verbose:
                    print(f"{p} -> HIT  -> {mem}")
            steps.append({"page": p, "hit": hit, "memory": mem[:]})
        if verbose:
            print(f"Total Page Faults: {faults}")
        return faults, steps


# ================= BANKER =================

class DeadlockManager:

    @staticmethod
    def bankers(n, m, alloc, maxm, avail, verbose=True):
        need = [[maxm[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
        finish = [False]*n
        seq = []
        work = avail[:]

        while len(seq) < n:
            found = False
            for i in range(n):
                if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += alloc[i][j]
                    seq.append(i)
                    finish[i] = True
                    found = True
            if not found:
                break

        is_safe = len(seq) == n
        if verbose:
            if is_safe:
                print("\nSystem is in SAFE state")
                print("Safe Sequence:", " -> ".join(f"P{i+1}" for i in seq))
            else:
                print("\nSystem is in DEADLOCK state")

        return {
            "safe": is_safe,
            "sequence": [f"P{i+1}" for i in seq],
            "need": need,
            "available_end": work
        }


# ================= DISPLAY =================

def print_result(n, at, bt, wt, tat, ct, gantt, pr=None):
    print("\n" + "="*85)
    print("            PROCESS SCHEDULING RESULT")
    print("="*85)

    if pr:
        print(f"\n{'P':<5}{'AT(ms)':<10}{'BT(ms)':<10}{'PR':<8}{'CT(ms)':<10}{'TAT(ms)':<10}{'WT(ms)':<10}")
    else:
        print(f"\n{'P':<5}{'AT(ms)':<10}{'BT(ms)':<10}{'CT(ms)':<10}{'TAT(ms)':<10}{'WT(ms)':<10}")

    print("-"*85)

    for i in range(n):
        if pr:
            print(f"P{i+1:<4}{at[i]:<10}{bt[i]:<10}{pr[i]:<8}{ct[i]:<10}{tat[i]:<10}{wt[i]:<10}")
        else:
            print(f"P{i+1:<4}{at[i]:<10}{bt[i]:<10}{ct[i]:<10}{tat[i]:<10}{wt[i]:<10}")

    print("-"*85)
    print(f"Average WT  : {sum(wt)/n:.2f} {TIME_UNIT}")
    print(f"Average TAT : {sum(tat)/n:.2f} {TIME_UNIT}")

    print("\nGantt Chart:")
    print(" ", end="")
    for _ in gantt:
        print("-------", end="")
    print()

    print("|", end="")
    for g in gantt:
        print(f"{g[0]:^7}|", end="")
    print()

    print(" ", end="")
    for _ in gantt:
        print("-------", end="")
    print()

    print(f"{gantt[0][1]}{TIME_UNIT}", end="   ")
    for g in gantt:
        print(f"{g[2]}{TIME_UNIT}", end="   ")
    print("\n")


# ================= MAIN =================

def main():
    while True:
        print("\n===== SMART OS RESOURCE MANAGER =====")
        print("1. CPU Scheduling")
        print("2. Memory Management")
        print("3. Deadlock Avoidance")
        print("4. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            print("\n1.FCFS 2.SJF 3.SRTF 4.Priority(Non-Preemptive) 5.Priority(Preemptive) 6.Round Robin")
            c = int(input("Choice: "))

            n = int(input("Processes: "))
            at = list(map(int, input("Arrival Times: ").split()))
            bt = list(map(int, input("Burst Times: ").split()))

            pr = None
            if c in [4,5]:
                pr = list(map(int, input("Priority: ").split()))
            if c == 6:
                q = int(input("Time Quantum: "))

            if c == 1:
                wt, tat, ct, g = Scheduler.fcfs(n, at, bt)
            elif c == 2:
                wt, tat, ct, g = Scheduler.sjf(n, at, bt)
            elif c == 3:
                wt, tat, ct, g = Scheduler.srtf(n, at, bt)
            elif c == 4:
                wt, tat, ct, g = Scheduler.priority_np(n, at, bt, pr)
            elif c == 5:
                wt, tat, ct, g = Scheduler.priority_p(n, at, bt, pr)
            else:
                wt, tat, ct, g = Scheduler.round_robin(n, at, bt, q)

            print_result(n, at, bt, wt, tat, ct, g, pr)

        elif ch == 2:
            print("\n1. FIFO  2. LRU")
            c = int(input("Choice: "))
            pages = list(map(int, input("Pages: ").split()))
            frames = int(input("Frames: "))

            if c == 1:
                MemoryManager.fifo(pages, frames)
            else:
                MemoryManager.lru(pages, frames)

        elif ch == 3:
            n = int(input("Processes: "))
            m = int(input("Resources: "))

            print("Allocation Matrix:")
            alloc = [list(map(int, input().split())) for _ in range(n)]

            print("Max Matrix:")
            maxm = [list(map(int, input().split())) for _ in range(n)]

            avail = list(map(int, input("Available: ").split()))

            DeadlockManager.bankers(n, m, alloc, maxm, avail)

        else:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()