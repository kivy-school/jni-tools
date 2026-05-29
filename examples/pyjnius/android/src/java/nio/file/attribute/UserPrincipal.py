from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserPrincipal"]

class UserPrincipal(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/UserPrincipal"