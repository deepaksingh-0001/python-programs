# Program: String Methods Demonstration

s = "deepak singh 1"

# Slicing & Reverse
print("Slicing [0:10] :", s[0:10])
print("Reverse         :", s[::-1])

# Basic Info
print("Length          :", len(s))
print("'deepak' in s   :", "deepak" in s)
print("'singh' not in s:", "singh" not in s)

# Case Conversion
print("Upper           :", s.upper())
print("Lower           :", s.lower())
print("Title           :", s.title())
print("Capitalize      :", s.capitalize())
print("Swapcase        :", s.swapcase())
print("Casefold        :", s.casefold())

# Space Handling
print("Strip           :", s.strip())
print("Lstrip          :", s.lstrip())
print("Rstrip          :", s.rstrip())

# Replace & Split
print("Replace         :", s.replace("singh", "rajput"))
print("Split           :", s.split())

# Search & Count
print("Find 'a'        :", s.find("a"))
print("Index 'a'       :", s.index("a"))
print("Count spaces    :", s.count(" "))

# Start / End Check
print("Endswith 'h'    :", s.endswith("h"))
print("Startswith ' '  :", s.startswith("d"))

# Join Example
s1 = ["deepak", "singh"]
print("Join            :", " ".join(s1))

# Type Checking
print("Is Alpha        :", s.isalpha())
print("Is Digit        :", s.isdigit())
print("Is Alnum        :", s.isalnum())

# Alignment & Formatting
print("Center          :", s.center(50))
print("Zfill           :", s.zfill(50))