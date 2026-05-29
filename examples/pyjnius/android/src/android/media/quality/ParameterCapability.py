from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParameterCapability"]

class ParameterCapability(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/quality/ParameterCapability"
    CAPABILITY_DEFAULT = JavaStaticField("Ljava/lang/String;")
    CAPABILITY_ENUM = JavaStaticField("Ljava/lang/String;")
    CAPABILITY_MAX = JavaStaticField("Ljava/lang/String;")
    CAPABILITY_MIN = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_DOUBLE = JavaStaticField("I")
    TYPE_INT = JavaStaticField("I")
    TYPE_LONG = JavaStaticField("I")
    TYPE_NONE = JavaStaticField("I")
    TYPE_STRING = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getParameterName = JavaMethod("()Ljava/lang/String;")
    getParameterType = JavaMethod("()I")
    isSupported = JavaMethod("()Z")
    getCapabilities = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")