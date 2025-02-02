from setuptools import find_packages, setup

HYPHON_E_DOT = "-e ."
def get_requirement(file_path: str)-> list[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements =file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements] 
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
    
    return requirements        
    


setup (
    name = 'mlproject',
    version="0.0.0.1",
    author="omprakash",
    author_email="op0454545@gmail.com",
    packages= find_packages(),
    install_requires=get_requirement("requirements.txt")
    
    
    
)