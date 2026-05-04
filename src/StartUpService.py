from os import makedirs, path, getcwd

class StartUpService:

    def __init__(self):
        pass
 
    
    def createResourcesDirectory(self):
        # Get the parent of the current working directory (src)
        parent_dir = path.dirname(getcwd())
        
        # Build the path to the sibling 'resources' directory
        resources_dir = path.join(parent_dir, "resources", "pictures")
        
        # Create the directory (exist_ok=True avoids errors if it already exists)
        makedirs(resources_dir, exist_ok=True)
            

    def setUp(self):
        self.createResourcesDirectory()