from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ConnectTimeoutException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ConnectTimeoutException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
    bytesTransferred = JavaField("I")