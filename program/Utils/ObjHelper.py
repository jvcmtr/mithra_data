from typing import Any, Type

# Created using AI

def create_instance(data: dict, cls: Type) -> Any:
    """
    Recursively creates an instance of a class from a dictionary, supporting nested objects.
    
    Args:
        data (dict): Dictionary of parameters.
        cls (type): The class to instantiate.
    
    Returns:
        An instance of cls.
    """
    from inspect import signature, _empty

    init_sig = signature(cls.__init__)
    kwargs = {}

    for name, param in init_sig.parameters.items():
        if name == 'self':
            continue

        if name in data:
            value = data[name]

            # If the parameter has a type hint and the value is a dict, recurse
            if isinstance(value, dict) and param.annotation != _empty and isinstance(param.annotation, type):
                kwargs[name] = create_instance(value, param.annotation)
            else:
                kwargs[name] = value

    return cls(**kwargs)


#   This class serves to allow dictionary access using . instead of [""]
#   Example usage:
#
#   dict = { "name" : "cicero" }
#   i = DotDict( dict )
#   print( i.name ) => outputs "cicero"
class object(dict):
    def __getattr__(self, key):
        return self.get(key, None)
    
    def __setattr__(self, name, value):
        self[name] = value
        
    def __getitem__(self, key):
        return self.get(key, None)