from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class PBEKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/PBEKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getIterationCount = JavaMethod("()I")
    getSalt = JavaMethod("()[B")
    getPassword = JavaMethod("()[C")

class DHPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/DHPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getX = JavaMethod("()Ljava/math/BigInteger;")

class DHPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/DHPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getY = JavaMethod("()Ljava/math/BigInteger;")

class DHKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/DHKey"
    getParams = JavaMethod("()Ljavax/crypto/spec/DHParameterSpec;")