import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import internal_parameters_entity as ipe

class InternalParameters():
    def __init__(self, entity=ipe.InternalParametersEntity()):
        self.entity = entity
        # self.cursor = super().cursor
        return


def main():
    pass



if __name__ == '__main__':
    main()