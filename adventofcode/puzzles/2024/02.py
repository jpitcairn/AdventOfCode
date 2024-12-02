from importlib.resources import read_text

def report_safety_check(report) -> bool:
    is_sorted = report == sorted(report) or report == sorted(report, reverse=True)
    is_safe_difference = all(1 <= abs(report[i] - report[i - 1]) <= 3 for i in range(1, len(report)))
    return is_sorted and is_safe_difference

def solve() -> tuple:
    # Open puzzle input and split into list
    data :list = read_text("adventofcode.resources.2024", "02.txt").strip().split("\n")

    reports :list = [list(map(int, line.split())) for line in data]

    safe_reports :list = []
    unsafe_reports :list = []
    corrected_reports :list = []

    for report in reports:
        if report_safety_check(report):
            safe_reports.append(report)
        else:
            unsafe_reports.append(report)

    for report in unsafe_reports:
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if report_safety_check(modified_report):
                corrected_reports.append(report)
                break

    total_safe_reports :int = len(safe_reports) + len(corrected_reports)

    return len(safe_reports), total_safe_reports
