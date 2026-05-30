from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LoginException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/login/LoginException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]