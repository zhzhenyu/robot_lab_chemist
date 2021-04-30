import numpy as np
import matplotlib.pyplot as plt
seq1 = np.mean((55.15, 55.30, 54.45))
htn1 = np.mean((93.29, 80.69, 83.80))
seq2 = np.mean((91.35, 84.97, 86.60))
htn2 = np.mean((97.28, 93.82, 94.42))
htn3 = np.mean((103.87, 98.73, 99.49))
seq3 = np.mean((108.66, 104.16, 107.32))
seq4 = np.mean((120.02, 128.36, 120.37))
htn4 = np.mean((119.79, 112.74, 108.76))
varseq1 = np.std((55.15, 55.30, 54.45))
varseq2 = np.std((91.35, 84.97, 86.60))
varseq3 = np.std((108.66, 104.16, 107.32))
varseq4 = np.std((120.02, 128.36, 120.37))
varhtn1 = np.std((93.29, 80.69, 83.80))
varhtn2 = np.std((97.28, 93.82, 94.42))
varhtn3 = np.std((103.87, 98.73, 99.49))
varhtn4 = np.std((119.79, 112.74, 108.76))
print(seq1,seq2,seq3,seq4,htn1,htn2,htn3,htn4)

# width of the bars
barWidth = 0.3

# Choose the height of the blue bars
bars1 = [seq1, seq2, seq3, seq4]

# Choose the height of the cyan bars
bars2 = [htn1, htn2, htn3, htn4]

# Choose the height of the error bars (bars1)
yer1 = [varseq1, varseq2, varseq3, varseq4]

# Choose the height of the error bars (bars2)
yer2 = [varhtn1, varhtn2, varhtn3, varhtn4]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

# Create blue bars
plt.bar(r1, bars1, width=barWidth, color='blue', edgecolor='black', yerr=yer1, capsize=7, label='Sequential')

# Create cyan bars
plt.bar(r2, bars2, width=barWidth, color='cyan', edgecolor='black', yerr=yer2, capsize=7, label='Hierarchical')

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1 Reaction', '2 Reactions', '3 Reactions', '4 Reactions'])
plt.ylabel('Time (s)')
plt.legend()

# Show graphic
plt.show()
