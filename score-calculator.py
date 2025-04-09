def avg(nums):
  """Calculates the average of a list of numbers."""
  return sum(nums) / len(nums) if nums else 0

# Example:
scores = [80, 90, 75, 85]
average = avg(scores)
print(f"Average: {average}")
