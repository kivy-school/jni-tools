from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PersonalizationData"]

class PersonalizationData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/PersonalizationData"

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/identity/PersonalizationData$Builder"
        __javaconstructor__ = [("()V", False)]
        addAccessControlProfile = JavaMethod("(Landroid/security/identity/AccessControlProfile;)Landroid/security/identity/PersonalizationData$Builder;")
        putEntry = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Collection;[B)Landroid/security/identity/PersonalizationData$Builder;")
        build = JavaMethod("()Landroid/security/identity/PersonalizationData;")