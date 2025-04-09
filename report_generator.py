def generate_feedback_report(feedback_list):
  """Generates a simple report from a list of feedback strings.

  Args:
    feedback_list: A list of strings, where each string is a piece of feedback.

  Returns:
    A string containing a basic summary of the feedback.
  """

  if not feedback_list:
    return "No feedback collected yet."

  report = "--- Feedback Report ---\n\n"
  report += f"Total feedback entries: {len(feedback_list)}\n\n"
  report += "Individual Feedback:\n"
  for i, feedback in enumerate(feedback_list):
    report += f"{i+1}. {feedback}\n"

  return report

# Example usage:
feedback = [
    "The website is very easy to use.",
    "I found the customer support helpful.",
    "The pricing could be more competitive.",
    "Great product overall!",
    "Navigation was a bit confusing."
]

report = generate_feedback_report(feedback)
print(report)
