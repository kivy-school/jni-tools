from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BidirectionalTypeConverter"]

class BidirectionalTypeConverter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/BidirectionalTypeConverter"
    __javaconstructor__ = [("(Ljava/lang/Class;Ljava/lang/Class;)V", False)]
    convertBack = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    invert = JavaMethod("()Landroid/animation/BidirectionalTypeConverter;")