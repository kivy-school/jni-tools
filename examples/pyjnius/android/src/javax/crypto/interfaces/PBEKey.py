from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PBEKey"]

class PBEKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/PBEKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getPassword = JavaMethod("()[C")
    getIterationCount = JavaMethod("()I")
    getSalt = JavaMethod("()[B")