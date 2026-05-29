from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyPath"]

class PropertyPath(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/PropertyPath"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/util/List;)V", False)]
    size = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    get = JavaMethod("(I)Landroid/app/appsearch/PropertyPath$PathSegment;")
    iterator = JavaMethod("()Ljava/util/Iterator;")

    class PathSegment(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/PropertyPath$PathSegment"
        NON_REPEATED_CARDINALITY = JavaStaticField("I")
        getPropertyIndex = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        create = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/app/appsearch/PropertyPath$PathSegment;", True, False), ("(Ljava/lang/String;)Landroid/app/appsearch/PropertyPath$PathSegment;", True, False)])
        getPropertyName = JavaMethod("()Ljava/lang/String;")