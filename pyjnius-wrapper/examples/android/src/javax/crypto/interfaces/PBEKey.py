from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PBEKey"]

class PBEKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/PBEKey"
    serialVersionUID = JavaStaticField("J")
    getPassword = JavaMethod("()[C")
    getSalt = JavaMethod("()[B")
    getIterationCount = JavaMethod("()I")