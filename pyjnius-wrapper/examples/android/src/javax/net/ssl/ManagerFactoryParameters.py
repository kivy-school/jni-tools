from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ManagerFactoryParameters"]

class ManagerFactoryParameters(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/ManagerFactoryParameters"