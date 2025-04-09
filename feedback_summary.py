from github import Github

def get_feedback_summary(repo, token):
  """Summarizes open GitHub issue titles and bodies."""
  g = Github(token)
  repo = g.get_repo(repo)
  feedback = {}
  for issue in repo.get_issues(state='open'):
    label = issue.labels[0].name if issue.labels else "General"
    feedback.setdefault(label, []).append(f"{issue.title}: {issue.body[:50]}...")
  return feedback

# --- REPLACE BELOW ---
repo_name = "your-username/your-repo"
github_token = "YOUR_GITHUB_TOKEN"
# ----------------------

summary = get_feedback_summary(repo_name, github_token)
for label, items in summary.items():
  print(f"\n**{label}:**")
  for item in items:
    print(f"- {item}")
