from app import app

# to refresh changes in the css, because it does not manually refresh
# code copied from https://stackoverflow.com/questions/9508667/reload-flask-app-when-template-file-changes
from os import path, walk

if __name__ == '__main__':

    # extra_dirs = ['directory/to/watch', ]
    # extra_files = extra_dirs[:]
    # for extra_dir in extra_dirs:
    #     for dirname, dirs, files in walk(extra_dir):
    #         for filename in files:
    #             filename = path.join(dirname, filename)
    #             if path.isfile(filename):
    #                 extra_files.append(filename)

    app.run(debug=True, extra_files='../static/custom.css')





