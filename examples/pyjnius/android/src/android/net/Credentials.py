from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Credentials"]

class Credentials(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/Credentials"
    __javaconstructor__ = [("(III)V", False)]
    getPid = JavaMethod("()I")
    getUid = JavaMethod("()I")
    getGid = JavaMethod("()I")