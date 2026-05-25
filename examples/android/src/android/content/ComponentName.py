from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ComponentName"]

class ComponentName(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ComponentName"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Landroid/content/Context;Ljava/lang/String;)V", False), ("(Landroid/content/Context;Ljava/lang/Class;)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    createRelative = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Landroid/content/ComponentName;", True, False), ("(Landroid/content/Context;Ljava/lang/String;)Landroid/content/ComponentName;", True, False)])
    clone = JavaMethod("()Landroid/content/ComponentName;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getClassName = JavaMethod("()Ljava/lang/String;")
    getShortClassName = JavaMethod("()Ljava/lang/String;")
    flattenToString = JavaMethod("()Ljava/lang/String;")
    flattenToShortString = JavaMethod("()Ljava/lang/String;")
    unflattenFromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/content/ComponentName;")
    toShortString = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    compareTo = JavaMethod("(Landroid/content/ComponentName;)I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMultipleMethod([("(Landroid/os/Parcel;I)V", False, False), ("(Landroid/content/ComponentName;Landroid/os/Parcel;)V", True, False)])
    readFromParcel = JavaStaticMethod("(Landroid/os/Parcel;)Landroid/content/ComponentName;")