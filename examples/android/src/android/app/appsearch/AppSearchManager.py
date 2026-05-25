from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSearchManager"]

class AppSearchManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/AppSearchManager"
    createSearchSession = JavaMethod("(Landroid/app/appsearch/AppSearchManager$SearchContext;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    createGlobalSearchSession = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    createEnterpriseGlobalSearchSession = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")

    class SearchContext(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchManager/SearchContext"
        getDatabaseName = JavaMethod("()Ljava/lang/String;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/AppSearchManager/SearchContext/Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            build = JavaMethod("()Landroid/app/appsearch/AppSearchManager$SearchContext;")