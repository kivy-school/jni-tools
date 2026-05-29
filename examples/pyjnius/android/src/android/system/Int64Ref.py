from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Int64Ref"]

class Int64Ref(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/Int64Ref"
    __javaconstructor__ = [("(J)V", False)]
    value = JavaField("J")
    toString = JavaMethod("()Ljava/lang/String;")