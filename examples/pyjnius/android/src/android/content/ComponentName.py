from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ComponentName"]

class ComponentName(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ComponentName"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Landroid/os/Parcel;)V", False), ("(Landroid/content/Context;Ljava/lang/String;)V", False), ("(Landroid/content/Context;Ljava/lang/Class;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Landroid/content/ComponentName;", False, False), ("()Ljava/lang/Object;", False, False)])
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/content/ComponentName;)I", False, False)])
    getPackageName = JavaMethod("()Ljava/lang/String;")
    toShortString = JavaMethod("()Ljava/lang/String;")
    getClassName = JavaMethod("()Ljava/lang/String;")
    createRelative = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Landroid/content/ComponentName;", True, False), ("(Landroid/content/Context;Ljava/lang/String;)Landroid/content/ComponentName;", True, False)])
    getShortClassName = JavaMethod("()Ljava/lang/String;")
    flattenToString = JavaMethod("()Ljava/lang/String;")
    flattenToShortString = JavaMethod("()Ljava/lang/String;")
    unflattenFromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/content/ComponentName;")
    writeToParcel = JavaMultipleMethod([("(Landroid/content/ComponentName;Landroid/os/Parcel;)V", True, False), ("(Landroid/os/Parcel;I)V", False, False)])
    readFromParcel = JavaStaticMethod("(Landroid/os/Parcel;)Landroid/content/ComponentName;")
    describeContents = JavaMethod("()I")