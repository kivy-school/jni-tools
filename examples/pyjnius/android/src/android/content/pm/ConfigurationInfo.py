from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConfigurationInfo"]

class ConfigurationInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ConfigurationInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/pm/ConfigurationInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    GL_ES_VERSION_UNDEFINED = JavaStaticField("I")
    INPUT_FEATURE_FIVE_WAY_NAV = JavaStaticField("I")
    INPUT_FEATURE_HARD_KEYBOARD = JavaStaticField("I")
    reqGlEsVersion = JavaField("I")
    reqInputFeatures = JavaField("I")
    reqKeyboardType = JavaField("I")
    reqNavigation = JavaField("I")
    reqTouchScreen = JavaField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getGlEsVersion = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")