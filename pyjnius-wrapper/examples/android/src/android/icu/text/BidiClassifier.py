from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BidiClassifier"]

class BidiClassifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/BidiClassifier"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False)]
    setContext = JavaMethod("(Ljava/lang/Object;)V")
    getContext = JavaMethod("()Ljava/lang/Object;")
    classify = JavaMethod("(I)I")