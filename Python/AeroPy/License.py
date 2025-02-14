# -*- coding: utf-8 -*-

import os.path


class LicenseLoader:
    __key_file_name = "key.lic"
    __license_file_name = "license.lic"
    __license_folder_name = "license"

    def __init__(self):
        self.__key = ""
        self.__license = ""
        ret = self.load_license()  # Return 0 is OK otherwise, it is an error
        if ret == 1:
            raise Exception("Error loading Key")
        elif ret == 2:
            raise Exception("Error loading License")
        elif ret == 3:
            raise Exception("Invalid key file format")

    def load_license(self) -> int:
        path_key = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                self.__license_folder_name, self.__key_file_name)
        if os.path.isfile(path_key):
            ret, self.__key = self.__load_license_file(path_key)
            if not ret:
                return 3
        else:
            return 1
        path_license = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    self.__license_folder_name, self.__key_file_name)
        if os.path.isfile(path_license):
            ret, self.__license = self.__load_license_file(path_license)
            if not ret:
                return 3
        else:
            return 2
        return 0

    @staticmethod
    def __load_license_file(file_name: str) -> (bool, str):
        # Open the file in read mode
        file = open(file_name, "r")
        # Read each line one by one
        line_counter = 0
        file_content = ""
        for line in file:
            file_content = line.strip()  # .strip() to remove newline characters
            line_counter += 1
        if line_counter != 1:  # Minified one line files
            return False, file_content
        # Close the file
        file.close()
        return True, file_content

    @property
    def key(self) -> str:
        return self.__key

    @property
    def license(self) -> str:
        return self.__license
