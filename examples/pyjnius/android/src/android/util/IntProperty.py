from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntProperty"]

class IntProperty(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/IntProperty"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    set = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;)V", False, False), ("(Ljava/lang/Object;Ljava/lang/Integer;)V", False, False)])
    setValue = JavaMethod("(Ljava/lang/Object;I)V")