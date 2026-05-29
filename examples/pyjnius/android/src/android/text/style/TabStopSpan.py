from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TabStopSpan"]

class TabStopSpan(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/TabStopSpan"
    getTabStop = JavaMethod("()I")

    class Standard(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/TabStopSpan/Standard"
        __javaconstructor__ = [("(I)V", False)]
        getTabStop = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")