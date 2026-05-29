from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppUriAuthenticationPolicy"]

class AppUriAuthenticationPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/AppUriAuthenticationPolicy"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAppAndUriMappings = JavaMethod("()Ljava/util/Map;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/AppUriAuthenticationPolicy$Builder"
        __javaconstructor__ = [("()V", False)]
        addAppAndUriMapping = JavaMethod("(Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;)Landroid/security/AppUriAuthenticationPolicy$Builder;")
        build = JavaMethod("()Landroid/security/AppUriAuthenticationPolicy;")