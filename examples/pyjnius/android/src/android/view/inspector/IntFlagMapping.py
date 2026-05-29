from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntFlagMapping"]

class IntFlagMapping(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/IntFlagMapping"
    __javaconstructor__ = [("()V", False)]
    add = JavaMethod("(IILjava/lang/String;)V")
    get = JavaMethod("(I)Ljava/util/Set;")