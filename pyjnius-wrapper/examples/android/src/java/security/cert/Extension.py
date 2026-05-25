from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Extension"]

class Extension(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/Extension"
    getId = JavaMethod("()Ljava/lang/String;")
    isCritical = JavaMethod("()Z")
    getValue = JavaMethod("()[B")
    encode = JavaMethod("(Ljava/io/OutputStream;)V")