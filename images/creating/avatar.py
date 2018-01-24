import pagan

# Create avatar using some text
img = pagan.Avatar("blackbat")

# Show created avatar
img.show()

# Use another hash function when generating avatar
# Default is MD5
img = pagan.Avatar("blackbat", pagan.SHA256)
img.show()