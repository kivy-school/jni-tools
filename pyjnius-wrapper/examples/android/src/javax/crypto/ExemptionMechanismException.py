from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExemptionMechanismException"]

class ExemptionMechanismException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/ExemptionMechanismException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]