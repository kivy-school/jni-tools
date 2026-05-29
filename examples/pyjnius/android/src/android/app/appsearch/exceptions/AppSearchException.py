from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSearchException"]

class AppSearchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/exceptions/AppSearchException"
    __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/Throwable;)V", False), ("(ILjava/lang/String;)V", False), ("(I)V", False)]
    getResultCode = JavaMethod("()I")
    toAppSearchResult = JavaMethod("()Landroid/app/appsearch/AppSearchResult;")