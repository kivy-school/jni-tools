from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSearchResult"]

class AppSearchResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/AppSearchResult"
    RESULT_ALREADY_EXISTS = JavaStaticField("I")
    RESULT_DENIED = JavaStaticField("I")
    RESULT_INTERNAL_ERROR = JavaStaticField("I")
    RESULT_INVALID_ARGUMENT = JavaStaticField("I")
    RESULT_INVALID_SCHEMA = JavaStaticField("I")
    RESULT_IO_ERROR = JavaStaticField("I")
    RESULT_NOT_FOUND = JavaStaticField("I")
    RESULT_OK = JavaStaticField("I")
    RESULT_OUT_OF_SPACE = JavaStaticField("I")
    RESULT_RATE_LIMITED = JavaStaticField("I")
    RESULT_SECURITY_ERROR = JavaStaticField("I")
    RESULT_UNKNOWN_ERROR = JavaStaticField("I")
    getResultCode = JavaMethod("()I")
    getErrorMessage = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    newFailedResult = JavaStaticMethod("(ILjava/lang/String;)Landroid/app/appsearch/AppSearchResult;")
    isSuccess = JavaMethod("()Z")
    newSuccessfulResult = JavaStaticMethod("(Ljava/lang/Object;)Landroid/app/appsearch/AppSearchResult;")
    getResultValue = JavaMethod("()Ljava/lang/Object;")