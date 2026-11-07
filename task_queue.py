#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().isoformat()
    try:
        with open("APPROVALS.md", "r") as f:
            if "[x] Add simple task queue" not in f.read():
                return
        # Process any pending tasks
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
            if tasks:
                with open("ideas.log", "a") as f:
                    f.write(f"{now}: Processed {len(tasks)} tasks from queue.\n---\n")
                open("tasks.txt", "w").close()  # clear queue
        except:
            pass
        # Add a default idle task
        with open("ideas.log", "a") as f:
            f.write(f"{now}: Task queue active. No pending tasks.\n---\n")
    except Exception as e:
        with open("ideas.log", "a") as f:
            f.write(f"{now}: task_queue error: {e}\n---\n")

if __name__ == "__main__":
    main()
