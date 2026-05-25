from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Prediction"]

class Prediction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/Prediction"
    name = JavaField("Ljava/lang/String;")
    score = JavaField("D")
    toString = JavaMethod("()Ljava/lang/String;")