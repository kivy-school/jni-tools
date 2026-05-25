from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FeatureInfo"]

class FeatureInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/FeatureInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/pm/FeatureInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_REQUIRED = JavaStaticField("I")
    GL_ES_VERSION_UNDEFINED = JavaStaticField("I")
    flags = JavaField("I")
    name = JavaField("Ljava/lang/String;")
    reqGlEsVersion = JavaField("I")
    version = JavaField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getGlEsVersion = JavaMethod("()Ljava/lang/String;")