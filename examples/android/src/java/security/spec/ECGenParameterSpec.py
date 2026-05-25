from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECGenParameterSpec"]

class ECGenParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECGenParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")