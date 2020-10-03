import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches



marks = [70, 45, 65, 55, 79, 91]
marks1 = [78, 64, 60, 84, 85, 95]
marksp = [87, 81, 96, 81, 94, 96]
marksp1 = [86, 70, 96, 73, 91, 91]
x = np.arange(len(marks))


fig = plt.figure(figsize=(10, 6.5))
barWidth = 0.2

plt.bar(x, marks, width=barWidth, color="green", zorder=2)
plt.bar(x + barWidth, marks1, width=barWidth, color="red", zorder=2)
plt.bar(x + barWidth*2, marksp, width=barWidth, color="black", zorder=2)
plt.bar(x + barWidth*3, marksp1, width=barWidth, color="blue", zorder=2)

plt.xticks(x + barWidth, ["English", "Hindi", "French", "Maths", "Science", "Social.Science"])
plt.title("""
TOCH PUBLIC SCHOOL
8th Grade Term-1 and Term-2
""")
plt.xlabel("Subjects")
plt.ylabel("Marks Obtained(out of 100)")
plt.grid(True)


greenp = mpatches.Patch(color="green", label='Cherish Term-1')
redp = mpatches.Patch(color="red", label='Cherish Term-2')
yellowp = mpatches.Patch(color="black", label='Prithvin Term-1')
bluep = mpatches.Patch(color="blue", label='Prithvin Term-2')
plt.legend(handles=[greenp, redp, yellowp, bluep], fontsize=6)
plt.show()
