"""
609. Find Duplicate File in System (Medium)

Given a list paths of directory info, including the directory path, and all the files with contents in
this directory, return all the duplicate files in the file system in terms of their paths.
You may return the answer in any order.

A group of duplicate files consists of at least **two** files that have the same content.

A single directory info string in the input list has the following format:

- "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are 'n' files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content)
respectively in the directory "root/d1/d2/.../dm".

Note that 'n' >= 1 and 'm' >= 0.
If 'm' = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths.
For each group, it contains all the file paths of the files that have the **same content**.
A file path is a string that has the following format:
    - "directory_path/file_name.txt"
"""

import collections


def findDuplicate(paths: list[str]) -> list[list[str]]:

    # content:[directory1, directory2,...]
    content_dict = collections.defaultdict(list)

    # Return file paths that have the same content
    for path in paths:
        s = path.split(" ", 1)  # splits into dir and files
        directory = s[0]
        files = s[1].split(" ")

        # Populate the content:[directory] dictionary
        for file in files:
            # Split on first parenthesis into filename and content and then strip the second parenthesis
            filename, content = file.split("(")
            content = content.rstrip(")")
            # Add directory to value list of this content
            content_dict[content].append(directory + "/" + filename)

    # Only add paths to result list if the sub-list is multiple items long (duplicates)
    return [i for i in list(content_dict.values()) if len(i) > 1]


def main():
    paths = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)",
    ]
    print(
        findDuplicate(paths),
        """
expected: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
""",
    )

    paths = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
    ]
    print(
        findDuplicate(paths),
        """
expected: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
""",
    )

    paths = [
        "root/a 1.txt(abcd) 2.txt(efsfgh)",
        "root/c 3.txt(abdfcd)",
        "root/c/d 4.txt(efggdfh)",
    ]
    print(
        findDuplicate(paths),
        """
expected: []
""",
    )


if __name__ == "__main__":
    main()
