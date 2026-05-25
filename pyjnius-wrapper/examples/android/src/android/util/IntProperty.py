from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntProperty"]

class IntProperty(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/IntProperty"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    setValue = JavaMethod("(Ljava/lang/Object;I)V")
    set = JavaMethod("(Ljava/lang/Object;Ljava/lang/Integer;)V")