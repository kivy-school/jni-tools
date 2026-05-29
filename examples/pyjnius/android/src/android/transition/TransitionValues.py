from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransitionValues"]

class TransitionValues(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/TransitionValues"
    __javaconstructor__ = [("()V", False), ("(Landroid/view/View;)V", False)]
    values = JavaField("Ljava/util/Map;")
    view = JavaField("Landroid/view/View;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")