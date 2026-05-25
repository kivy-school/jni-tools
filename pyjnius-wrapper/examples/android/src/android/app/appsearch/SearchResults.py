from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchResults"]

class SearchResults(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SearchResults"
    getNextPage = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    close = JavaMethod("()V")