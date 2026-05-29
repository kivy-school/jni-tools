from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PasswordAuthentication"]

class PasswordAuthentication(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/PasswordAuthentication"
    __javaconstructor__ = [("(Ljava/lang/String;[C)V", False)]
    getUserName = JavaMethod("()Ljava/lang/String;")
    getPassword = JavaMethod("()[C")