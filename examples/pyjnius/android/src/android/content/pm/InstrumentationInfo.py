from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    banner = JavaField("I")
    icon = JavaField("I")
    isArchived = JavaField("Z")
    labelRes = JavaField("I")
    logo = JavaField("I")
    metaData = JavaField("Landroid/os/Bundle;")
    name = JavaField("Ljava/lang/String;")
    nonLocalizedLabel = JavaField("Ljava/lang/CharSequence;")
    packageName = JavaField("Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")