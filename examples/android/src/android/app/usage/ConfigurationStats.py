from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConfigurationStats"]

class ConfigurationStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/ConfigurationStats"
    __javaconstructor__ = [("(Landroid/app/usage/ConfigurationStats;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getConfiguration = JavaMethod("()Landroid/content/res/Configuration;")
    getFirstTimeStamp = JavaMethod("()J")
    getLastTimeStamp = JavaMethod("()J")
    getLastTimeActive = JavaMethod("()J")
    getTotalTimeActive = JavaMethod("()J")
    getActivationCount = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")