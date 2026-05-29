from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppOwnedSdkSandboxInterface"]

class AppOwnedSdkSandboxInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/AppOwnedSdkSandboxInterface"
    __javaconstructor__ = [("(Ljava/lang/String;JLandroid/os/IBinder;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    getInterface = JavaMethod("()Landroid/os/IBinder;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getVersion = JavaMethod("()J")