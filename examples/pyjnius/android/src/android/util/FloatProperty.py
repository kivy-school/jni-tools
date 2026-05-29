from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloatProperty"]

class FloatProperty(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/FloatProperty"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    set = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;)V", False, False), ("(Ljava/lang/Object;Ljava/lang/Float;)V", False, False)])
    setValue = JavaMethod("(Ljava/lang/Object;F)V")