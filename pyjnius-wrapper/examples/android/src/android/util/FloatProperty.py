from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloatProperty"]

class FloatProperty(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/FloatProperty"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    setValue = JavaMethod("(Ljava/lang/Object;F)V")
    set = JavaMethod("(Ljava/lang/Object;Ljava/lang/Float;)V")