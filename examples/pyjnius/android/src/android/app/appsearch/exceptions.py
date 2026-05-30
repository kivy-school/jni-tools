from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AppSearchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/exceptions/AppSearchException"
    __javaconstructor__ = [("(I)V", False), ("(ILjava/lang/String;Ljava/lang/Throwable;)V", False), ("(ILjava/lang/String;)V", False)]
    getResultCode = JavaMethod("()I")
    toAppSearchResult = JavaMethod("()Landroid/app/appsearch/AppSearchResult;")