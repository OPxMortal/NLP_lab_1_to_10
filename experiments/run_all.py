import subprocess
import os

inputs = {
    "exp1.py": "The striped bats were hanging upside down for eating small insects.\n",
    "exp2.py": "The quick brown fox jumps over the lazy dog.\n",
    "exp3.py": "4\nGovernment announces new economic policy\nEconomy grows as government releases new policy\nLocal team wins championship match\nSports team celebrates victory in final match\ndog\ncat\n",
    "exp4.py": "3\nArtificial intelligence and machine learning are revolutionizing technology.\nDeep learning models require extensive computational resources.\nHealthy diet and exercise improve overall well being.\nmachine learning and artificial intelligence\n",
    "exp5.py": "Supreme Court of India delivered judgment in New Delhi regarding Article 370 on Monday.\n4\n",
    "exp6.py": "Aspirin treats headache and reduces inflammation in patients.\n1\n"
}

output_text = "=========================================================\n"
output_text += "     NLP LAB EXPERIMENTS 1 TO 6 RUNTIME OUTPUTS\n"
output_text += "=========================================================\n\n"

exp_dir = os.path.dirname(os.path.abspath(__file__))

for exp in ["exp1.py", "exp2.py", "exp3.py", "exp4.py", "exp5.py", "exp6.py"]:
    filepath = os.path.join(exp_dir, exp)
    output_text += f"#########################################################\n"
    output_text += f"### {exp.upper()} OUTPUT\n"
    output_text += f"#########################################################\n"
    
    inp = inputs[exp]
    output_text += f"INPUT PROVIDED:\n{inp.strip()}\n"
    output_text += "-" * 40 + "\n"
    
    res = subprocess.run(["python", filepath], input=inp, capture_output=True, text=True)
    if res.stdout:
        output_text += f"STDOUT:\n{res.stdout}\n"
    if res.stderr:
        output_text += f"STDERR:\n{res.stderr}\n"
    output_text += "\n"

output_file = os.path.join(exp_dir, "OUTPUT_EXP1_TO_6.txt")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(output_text)

print("Execution finished. Output saved to OUTPUT_EXP1_TO_6.txt")
