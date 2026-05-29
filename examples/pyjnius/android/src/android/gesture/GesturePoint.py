from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GesturePoint"]

class GesturePoint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/GesturePoint"
    __javaconstructor__ = [("(FFJ)V", False)]
    timestamp = JavaField("J")
    x = JavaField("F")
    y = JavaField("F")
    clone = JavaMethod("()Ljava/lang/Object;")