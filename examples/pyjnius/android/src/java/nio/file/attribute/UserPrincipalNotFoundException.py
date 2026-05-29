from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserPrincipalNotFoundException"]

class UserPrincipalNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/UserPrincipalNotFoundException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")