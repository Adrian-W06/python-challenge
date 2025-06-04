
import pandas as pd
import os
import pandas as pd


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "C:\\Users\\bnewz\\Downloads\\Repo\\Python-Challenge\\Pypoll\\Resouces\\election_data.csv")


df = pd.read_csv(file_path)


total_votes = df.shape[0]

vote_counts = df["Candidate"].value_counts()


vote_percentages = (vote_counts / total_votes) * 100


winner = vote_counts.idxmax()

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in vote_counts.index:
    percentage = vote_percentages[candidate]
    votes = vote_counts[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")




lines = []
lines.append("Election Results")
lines.append("-------------------------")
lines.append(f"Total Votes: {total_votes}")
lines.append("-------------------------")
for candidate in vote_counts.index:
    percentage = vote_percentages[candidate]
    votes = vote_counts[candidate]
    lines.append(f"{candidate}: {percentage:.3f}% ({votes})")
lines.append("-------------------------")
lines.append(f"Winner: {winner}")
lines.append("-------------------------")

# Print to terminal
for line in lines:
    print(line)

# Export to text file
output_path = os.path.join(script_dir, "election_results.txt")
with open(output_path, "w") as f:
    for line in lines:
        f.write(line + "\n")