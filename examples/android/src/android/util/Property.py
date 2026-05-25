from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Property"]

class Property(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Property"
    __javaconstructor__ = [("(Ljava/lang/Class;Ljava/lang/String;)V", False)]
    of = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/Class;Ljava/lang/String;)Landroid/util/Property;")
    isReadOnly = JavaMethod("()Z")
    set = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    getName = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/Class;")