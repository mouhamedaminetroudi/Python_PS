# Description:
# Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway
# ===================
def remove_trailing_zeros(n):
    if n == 0:
        return 0
    return int(str(n).rstrip('0'))

# Test cases
print(remove_trailing_zeros(1450))      # 145