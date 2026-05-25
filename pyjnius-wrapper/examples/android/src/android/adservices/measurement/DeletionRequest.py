from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeletionRequest"]

class DeletionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/DeletionRequest"
    DELETION_MODE_ALL = JavaStaticField("I")
    DELETION_MODE_EXCLUDE_INTERNAL_DATA = JavaStaticField("I")
    MATCH_BEHAVIOR_DELETE = JavaStaticField("I")
    MATCH_BEHAVIOR_PRESERVE = JavaStaticField("I")
    getOriginUris = JavaMethod("()Ljava/util/List;")
    getDomainUris = JavaMethod("()Ljava/util/List;")
    getDeletionMode = JavaMethod("()I")
    getMatchBehavior = JavaMethod("()I")
    getStart = JavaMethod("()Ljava/time/Instant;")
    getEnd = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/DeletionRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        setOriginUris = JavaMethod("(Ljava/util/List;)Landroid/adservices/measurement/DeletionRequest$Builder;")
        setDomainUris = JavaMethod("(Ljava/util/List;)Landroid/adservices/measurement/DeletionRequest$Builder;")
        setMatchBehavior = JavaMethod("(I)Landroid/adservices/measurement/DeletionRequest$Builder;")
        setDeletionMode = JavaMethod("(I)Landroid/adservices/measurement/DeletionRequest$Builder;")
        setStart = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/measurement/DeletionRequest$Builder;")
        setEnd = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/measurement/DeletionRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/measurement/DeletionRequest;")