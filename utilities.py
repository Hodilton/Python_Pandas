import os

class Utilities:
    class Data:
        @staticmethod
        def pre_check(data_load_params):
            folder_path = data_load_params.get('folder_path', '')
            file_name = data_load_params.get('file_name', '')

            if not folder_path:
                Utilities.Raise.folder_specified_error()
                return None

            if not file_name:
                Utilities.Raise.file_name_specified_error()
                return None

            if not Utilities.Check.directory_exists(folder_path):
                Utilities.Raise.folder_found_error(folder_path)
                return None

            data_path = os.path.join(folder_path, file_name)

            if not Utilities.Check.file_exists(data_path):
                Utilities.Raise.file_found_error(data_path)
                return None

            return data_path

    class Raise:
        @staticmethod
        def folder_specified_error():
            print(f"'folder_path' not specified.")

        @staticmethod
        def file_name_specified_error():
            print(f"'file_name' not specified.")

        @staticmethod
        def file_found_error(file_path):
            print(f"File '{file_path}' not found.")

        @staticmethod
        def folder_found_error(folder_path):
            print(f"Folder '{folder_path}' not found.")

        @staticmethod
        def data_load_error():
            print(f"Data is not loaded.")

        @staticmethod
        def graph_key_error(key):
            print(f"Invalid graph key: {key} .")

    class Check:
        @staticmethod
        def directory_exists(folder_path):
            return os.path.exists(folder_path)

        @staticmethod
        def file_exists(file_path):
            return os.path.isfile(file_path)

        # @staticmethod
        # def check_image_filename(file_name):
        #     return file_name.endswith(('.jpg', '.jpeg', '.png', '.bmp'))
        #
        # @staticmethod
        # def images_found_error(folder_path):
        #     print(f"No images found in folder '{folder_path}\\'.")
