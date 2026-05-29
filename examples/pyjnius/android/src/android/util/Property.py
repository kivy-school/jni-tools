from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Property"]

class Property(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Property"
    __javaconstructor__ = [("(Ljava/lang/Class;Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    of = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/Class;Ljava/lang/String;)Landroid/util/Property;")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    set = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")
    getType = JavaMethod("()Ljava/lang/Class;")
    isReadOnly = JavaMethod("()Z")