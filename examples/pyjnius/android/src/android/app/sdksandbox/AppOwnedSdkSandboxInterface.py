from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppOwnedSdkSandboxInterface"]

class AppOwnedSdkSandboxInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/AppOwnedSdkSandboxInterface"
    __javaconstructor__ = [("(Ljava/lang/String;JLandroid/os/IBinder;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getName = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()J")
    getInterface = JavaMethod("()Landroid/os/IBinder;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")