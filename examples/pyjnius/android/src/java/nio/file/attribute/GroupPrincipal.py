from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GroupPrincipal"]

class GroupPrincipal(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/GroupPrincipal"