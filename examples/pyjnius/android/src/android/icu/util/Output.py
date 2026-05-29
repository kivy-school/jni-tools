from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Output"]

class Output(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/Output"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/Object;)V", False)]
    value = JavaField("Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")