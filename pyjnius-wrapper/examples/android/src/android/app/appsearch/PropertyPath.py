from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyPath"]

class PropertyPath(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/PropertyPath"
    __javaconstructor__ = [("(Ljava/util/List;)V", False), ("(Ljava/lang/String;)V", False)]
    get = JavaMethod("(I)Landroid/app/appsearch/PropertyPath$PathSegment;")
    size = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class PathSegment(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/PropertyPath/PathSegment"
        NON_REPEATED_CARDINALITY = JavaStaticField("I")
        create = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/app/appsearch/PropertyPath$PathSegment;", True, False), ("(Ljava/lang/String;)Landroid/app/appsearch/PropertyPath$PathSegment;", True, False)])
        getPropertyName = JavaMethod("()Ljava/lang/String;")
        getPropertyIndex = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")