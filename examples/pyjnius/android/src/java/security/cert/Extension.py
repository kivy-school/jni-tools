from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Extension"]

class Extension(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/Extension"
    encode = JavaMethod("(Ljava/io/OutputStream;)V")
    getValue = JavaMethod("()[B")
    getId = JavaMethod("()Ljava/lang/String;")
    isCritical = JavaMethod("()Z")