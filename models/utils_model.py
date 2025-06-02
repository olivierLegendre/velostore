import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")
import entity_manager as em

class UtilsModel:
    def __init__(self, connector):
        entity_manager = em.EntityManager(connector)
        entity = entity_manager.get_entity(self.get_names())
        self.entity = entity
        self.connector = connector
    
    def get_names(self):
        model_class_name_value = self.__class__.__name__
        model_name_value= ''.join(['_' + char.lower() if char.isupper() else char for char in model_class_name_value])
        if model_name_value.startswith("_"):
            model_name_value = model_name_value[1:]
        
        return dict(
            model_class_name = self.__class__.__name__,
            entity_class_name = self.__class__.__name__+"Entity",
            model_name = model_name_value,
            entity_name = model_name_value+"_entity",
            
        )
    
def main():
    pass

if __name__ == '__main__':
    main()