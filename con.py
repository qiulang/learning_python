#! /usr/bin/env python3
import queue


def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")
    print(f"Task {name} done")


def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of work
    work_queue = queue.Queue()

    # Put some work in the queue
    for work in [15, 14, 5, 2]:
        work_queue.put(work)

    # Create some tasks
    tasks = [task("One", work_queue), task("Two", work_queue)]
    #tasks = [(task, "One", work_queue), (task, "Two", work_queue)]

    # Run the tasks
    done = False
    print("start the while loop")
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == "__main__":
    main()
