from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeConverter"]

class TypeConverter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TypeConverter"
    __javaconstructor__ = [("(Ljava/lang/Class;Ljava/lang/Class;)V", False)]
    convert = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")