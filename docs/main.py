# in this directory ,there are some folder and files and in that folder there are some files 
# in all the files ,if content is missing ,then write the content in that file with given content but file name should be same:

import os

# Function to add content to files
def add_content_to_files(content):
    current_dir = os.getcwd()  # Get the current directory
    for subdir, _, files in os.walk(current_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            with open(file_path, 'a') as f:
                f.seek(0, 2)  # Go to the end of the file
                if f.tell() == 0:  # Check if the file is empty
                    f.write(content)

if __name__ == "__main__":
    content_to_add = """

This page is currently under development, and content will be added soon. Thank you for your patience!

If you are interested in contributing to the development of these notes, please fill out our [Google Form](https://forms.gle/bhYV5PZjsjVnrcWZ9) to express your interest.

Feel free to [contact us](mailto:bandaru.sanjay@bba.christuniversity.in) if you have any questions or suggestions.

<!-- You can add more details or sections as needed -->
"""

    add_content_to_files(content_to_add)
