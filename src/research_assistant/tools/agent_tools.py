import os
import re
from datetime import datetime
from pathlib import Path


def save_to_file(report_content: str, topic: str)-> dict [str, str] | None:
    """
    Takes report_content and topic as input arguments, and returns status as success or error.
    Use this tool when user asked to use save_to_file tool.
    """

    # Set the topic for a filename
    clean_topic = re.sub(r'[^\w\s-]', '', topic)
    clean_topic = re.sub(r'[\s-]+', '_', clean_topic).strip('_')
    clean_topic = clean_topic[:30]  # Limit length for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_base = f"research_report_{clean_topic}_{timestamp}"

    # Get current working dir
    cwd = Path.cwd()

    # Get the path of the parent directory
    parent_dir = cwd.parent

    # Build report folder path
    report_folder_path = parent_dir / "reports"

    # Create folder, if does not exist
    os.makedirs(report_folder_path, exist_ok=True)

    # Set report file name
    filename = os.path.join(report_folder_path, f"{filename_base}.md")
    try:
        # Create report file in report folder
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
        print(f"\nReport saved as: {filename_base}.md")
        return {"status": "success"}
    except Exception as e:
        err = f"\nError saving report to text file: {e}"
        print(err)
        return {"status": err}


def get_current_date() -> str:
    """
    Returns the current date in 'Weekday, Month DD, YYYY' format.
    Use this tool whenever the user asks for 'today', 'today's date', 'now', or the 'current date'.
    """
    return datetime.now().strftime("%A, %B %d, %Y")