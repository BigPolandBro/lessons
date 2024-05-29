import os

def find_all_catalog_files_recursively(dir_path = '.'):
    file_paths = []
    
    def helper(dir_path):
        names = os.listdir(dir_path)
        for name in names:
            if name.startswith('.'):
                continue
            path = os.path.join(dir_path, name)
            if os.path.isdir(path):
                helper(path)
            else:
                file_paths.append(path)
        return file_paths
    
    helper(dir_path)
    return file_paths

# to check
cut_dir_name = '~/Desktop/test_root'
dir_name = os.path.expanduser(cut_dir_name)
find_all_catalog_files_recursively(dir_name)
