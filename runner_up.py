# Task 3: Runner-up score
# Read n and n scores, then print the second-highest distinct score

n = int(input())                                  # number of scores
scores = list(map(int, input().split()))[:n]      # read n scores from one line
distinct = sorted(set(scores), reverse=True)      # remove duplicates, sort high to low
print(distinct[1])                                # second-highest distinct score