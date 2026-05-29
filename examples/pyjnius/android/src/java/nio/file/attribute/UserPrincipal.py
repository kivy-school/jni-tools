from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserPrincipal"]

class UserPrincipal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/UserPrincipal"