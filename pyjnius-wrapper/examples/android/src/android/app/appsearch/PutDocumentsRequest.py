from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PutDocumentsRequest"]

class PutDocumentsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/PutDocumentsRequest"
    getGenericDocuments = JavaMethod("()Ljava/util/List;")
    getTakenActionGenericDocuments = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/PutDocumentsRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        addGenericDocuments = JavaMultipleMethod([("([Landroid/app/appsearch/GenericDocument;)Landroid/app/appsearch/PutDocumentsRequest$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/PutDocumentsRequest$Builder;", False, False)])
        addTakenActionGenericDocuments = JavaMultipleMethod([("([Landroid/app/appsearch/GenericDocument;)Landroid/app/appsearch/PutDocumentsRequest$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/PutDocumentsRequest$Builder;", False, False)])
        build = JavaMethod("()Landroid/app/appsearch/PutDocumentsRequest;")