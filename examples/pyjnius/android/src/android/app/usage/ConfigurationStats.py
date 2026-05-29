from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConfigurationStats"]

class ConfigurationStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/ConfigurationStats"
    __javaconstructor__ = [("(Landroid/app/usage/ConfigurationStats;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLastTimeActive = JavaMethod("()J")
    getActivationCount = JavaMethod("()I")
    getTotalTimeActive = JavaMethod("()J")
    getFirstTimeStamp = JavaMethod("()J")
    getLastTimeStamp = JavaMethod("()J")
    getConfiguration = JavaMethod("()Landroid/content/res/Configuration;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")