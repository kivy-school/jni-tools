from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ManagerFactoryParameters"]

class ManagerFactoryParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/ManagerFactoryParameters"