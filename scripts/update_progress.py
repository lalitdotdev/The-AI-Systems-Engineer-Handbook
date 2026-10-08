#!/usr/bin/env python3
"""Update personal learning progress tracker."""

import argparse
import datetime
import re
from pathlib import Path

def update_progress(lesson_slug: str, status: str, tracker_path: Path = None):
    """Update or create a personal learning tracker."""
    if tracker_path is None:
        tracker_path = Path.home() / ".ai-engineering-progress.md"

    # Load existing or create template
    if tracker_path.exists():
        content = tracker_path.read_text()
    else:
        content = f"""# 📈 My AI Engineering Progress

*Updated: {datetime.date.today()}*

## ✅ Completed Lessons
- [ ] (none yet)

## 📚 In Progress
- [ ] (none yet)

## ⬜ Not Started
<!-- Auto-generated list of all lessons would go here -->
"""

    # Parse current state
    lines = content.split('\n')
    in_completed = False
    in_progress = False

    new_lines = []
    for line in lines:
        if line.startswith('## ✅ Completed Lessons'):
            in_completed = True
            in_progress = False
        elif line.startswith('## 📚 In Progress'):
            in_completed = False
            in_progress = True
        elif line.startswith('## ⬜ Not Started'):
            in_completed = False
            in_progress = False

        # Skip the lesson item lines (we'll rebuild them)
        if line.strip().startswith('- [') and (in_completed or in_progress):
            continue

        new_lines.append(line)

    # Add the updated item
    marker = '[x]' if status == 'completed' else '[ ]'
    section = 'Completed Lessons' if status == 'completed' else 'In Progress'
    new_item = f'- {marker} {lesson_slug}'

    # Insert in the right section
    final_lines = []
    for line in new_lines:
        final_lines.append(line)
        if line.startswith(f'## ✅ {section}') and status == 'completed':
            final_lines.append(new_item)
        elif line.startswith(f'## 📚 {section}') and status == 'in_progress':
            final_lines.append(new_item)

    # Update timestamp
    final_lines[1] = f"*Updated: {datetime.date.today()}*"

    tracker_path.write_text('\n'.join(final_lines))
    print(f"✅ Updated {tracker_path}: {lesson_slug} -> {status}")

def main():
    parser = argparse.ArgumentParser(description="Update AI Engineering progress")
    parser.add_argument("--lesson", required=True, help="Lesson slug (e.g., 01-python-fundamentals)")
    parser.add_argument("--status", choices=["completed", "in_progress"], required=True)
    parser.add_argument("--tracker", help="Path to tracker file")

    args = parser.parse_args()
    tracker_path = Path(args.tracker) if args.tracker else None
    update_progress(args.lesson, args.status, tracker_path)

if __name__ == "__main__":
    main()