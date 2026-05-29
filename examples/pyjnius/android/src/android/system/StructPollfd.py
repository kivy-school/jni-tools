from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructPollfd"]

class StructPollfd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructPollfd"
    __javaconstructor__ = [("()V", False)]
    events = JavaField("S")
    fd = JavaField("Ljava/io/FileDescriptor;")
    revents = JavaField("S")
    userData = JavaField("Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")