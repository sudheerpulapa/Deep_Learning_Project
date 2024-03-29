# Importing necessary functions from the setuptools library
from setuptools import find_packages, setup

# Importing List type from the typing module
from typing import List

# Defining a constant variable HYPEN_E_DOT with a specific value
HYPEN_E_DOT = '-e .'

# Defining a function called get_requirements that takes a file path as input
# and returns a list of requirements (dependencies) for the project
def get_requirements(file_path: str) -> List[str]:
    # Creating an empty list called requirements
    requirements = []
    
    # Opening the file at the given file path
    with open(file_path) as file_obj:
        # Reading all lines from the file and storing them in the requirements list
        requirements = file_obj.readlines()
        
        # Removing the newline character ("\n") from each requirement and updating the list
        requirements = [req.replace("\n", "") for req in requirements]

        # Checking if the constant HYPEN_E_DOT exists in the list of requirements
        if HYPEN_E_DOT in requirements:
            # If it exists, removing it from the list
            requirements.remove(HYPEN_E_DOT)

    # Returning the list of requirements
    return requirements

# Calling the setup function from setuptools to configure our project
setup(
    # Specifying the name of the project
    name="X_Ray",
    
    # Specifying the version of the project
    version="0.0.1",
    
    # Specifying the author of the project
    author="Sudheer Chowdary Pulapa",
    
    # Specifying the email of the author
    author_email="sudheerpulapa@gmail.com",
    
    # Calling the get_requirements function to get the list of dependencies
    # from the specified file path and setting it as install_requires
    install_requires=get_requirements(r"C:\\Users\\Sudheer Pulapa\\deeplearningproject\\Deep_Learning_Project\\requirements_dev.txt"),
    
    # Automatically finding all packages in the project
    packages=find_packages()
)
