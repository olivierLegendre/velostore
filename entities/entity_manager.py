import importlib.util
import sys
import string
import secrets

class EntityManager():
    connectors =  ['sqlite', 'mongodb']
    def __init__(self, connector='sqlite'):
        if connector in self.connectors:
            # print(f"on se connecte sur {connector}")
            self.connector = connector
        else: 
            print(f"connector {connector} is not yet available")
        pass
    
    def get_entity_path(self, entity_name):
        match self.connector:
            case 'sqlite':
                return 'entities/sqlite/'+entity_name+'.py'
            case 'mongodb':
                return 'entities/mongodb/'+entity_name+'.py'
        
    def get_entity(self, names):    
        entity_path = self.get_entity_path(names["entity_name"])
        module = self.load_module(entity_path)
        entity = getattr(module, names["entity_class_name"])
        return entity()
        
    def load_database(self):
        match self.connector:
            case 'sqlite':
                return self.load_module('db/sqlite_database.py')
            case 'mongodb':
                return self.load_module('db/mongodb_database.py')
        
        
    def gensym(self, length=32, prefix="gensym_"):
        """
        generates a fairly unique symbol, used to make a module name,
        used as a helper function for load_module

        :return: generated symbol
        """
        alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
        symbol = "".join([secrets.choice(alphabet) for i in range(length)])

        return prefix + symbol


    def load_module(self, source, module_name=None):
        """
        reads file source and loads it as a module

        :param source: file to load
        :param module_name: name of module to register in sys.modules
        :return: loaded module
        """

        if module_name is None:
            module_name = self.gensym()

        spec = importlib.util.spec_from_file_location(module_name, source)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        return module
    

def main():
    pass
if __name__ == '__main__':
    main()