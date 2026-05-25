from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InstrumentationInfo"]

class InstrumentationInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/InstrumentationInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/pm/InstrumentationInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    dataDir = JavaField("Ljava/lang/String;")
    functionalTest = JavaField("Z")
    handleProfiling = JavaField("Z")
    publicSourceDir = JavaField("Ljava/lang/String;")
    sourceDir = JavaField("Ljava/lang/String;")
    splitNames = JavaField("[Ljava/lang/String;")
    splitPublicSourceDirs = JavaField("[Ljava/lang/String;")
    splitSourceDirs = JavaField("[Ljava/lang/String;")
    targetPackage = JavaField("Ljava/lang/String;")
    targetProcesses = JavaField("Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")