from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BidiClassifier"]

class BidiClassifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/BidiClassifier"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False)]
    setContext = JavaMethod("(Ljava/lang/Object;)V")
    classify = JavaMethod("(I)I")
    getContext = JavaMethod("()Ljava/lang/Object;")