from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppUriAuthenticationPolicy"]

class AppUriAuthenticationPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/AppUriAuthenticationPolicy"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getAppAndUriMappings = JavaMethod("()Ljava/util/Map;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/AppUriAuthenticationPolicy/Builder"
        __javaconstructor__ = [("()V", False)]
        addAppAndUriMapping = JavaMethod("(Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;)Landroid/security/AppUriAuthenticationPolicy$Builder;")
        build = JavaMethod("()Landroid/security/AppUriAuthenticationPolicy;")