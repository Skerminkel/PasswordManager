# a_dict = {"key": "value"}
#
# try:
#     file = open("a_file.txt")
#     print(a_dict['asdf'])
#
# except FileNotFoundError:
#
#     file = open("a_file.txt", "a")
#     file.write("a_dict = {}\n")
#     file.close()
#
# except KeyError as error:
#
#     file = open("a_file.txt", "a")
#     file.write(f"a_dict[{error}] = something")
#
# else:
#     content = file.read()
#     print(content)

