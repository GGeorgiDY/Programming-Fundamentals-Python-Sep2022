path_to_a_file = input().split("\\")

file_name_and_extension = path_to_a_file[-1]
file_name = file_name_and_extension.split(".")[0]
extension = file_name_and_extension.split(".")[1]
print(f"File name: {file_name}")
print(f"File extension: {extension}")

# C:\Internal\training-internal\Template.pptx
# ->
# File name: Template
# File extension: pptx
