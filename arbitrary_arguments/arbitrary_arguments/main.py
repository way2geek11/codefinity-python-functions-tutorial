def generate_report(*scores, **kwargs):
    label = kwargs.get("label", "Report")
    avg = sum(scores)/len(scores)
    if "passing_score" in kwargs:
        status = "Status: Pass" if avg >= kwargs["passing_score"] else "Status: Fail"
        return f"{label} | Average: {avg:.2f} | {status}"

    return f"{label} | Average: {avg:.2f}"

# Testing the result
print(generate_report(80, 90, 70, label="Math", passing_score=75))
print(generate_report(50, 60, 40, passing_score=65))
print(generate_report(95, 88, 92, label="Science"))