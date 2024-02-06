import os
def find_all_files(directory):
    for cur_dir, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(cur_dir, file)
if __name__ == '__main__':
    for file in find_all_files('.\\'):
        if file[:7] == ".\_site" and file[-5:] == ".html":
            with open(file, encoding="utf-8") as reader:
                content = reader.read()
            content = content.replace("href=\"/", "href=\"https://harry-arbrebleu.github.io/test3/")
            content = content.replace("src=\"/", "src=\"https://harry-arbrebleu.github.io/test3/")
            with open(file, 'w', encoding="utf-8") as writer:
                writer.write(content)