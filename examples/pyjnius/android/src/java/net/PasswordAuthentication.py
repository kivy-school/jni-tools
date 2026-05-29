from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PasswordAuthentication"]

class PasswordAuthentication(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/PasswordAuthentication"
    __javaconstructor__ = [("(Ljava/lang/String;[C)V", False)]
    getPassword = JavaMethod("()[C")
    getUserName = JavaMethod("()Ljava/lang/String;")