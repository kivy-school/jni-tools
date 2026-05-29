from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GroupPrincipal"]

class GroupPrincipal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/GroupPrincipal"