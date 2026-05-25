from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseBundle"]

class BaseBundle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/BaseBundle"
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    clear = JavaMethod("()V")
    containsKey = JavaMethod("(Ljava/lang/String;)Z")
    get = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    remove = JavaMethod("(Ljava/lang/String;)V")
    putAll = JavaMethod("(Landroid/os/PersistableBundle;)V")
    keySet = JavaMethod("()Ljava/util/Set;")
    putBoolean = JavaMethod("(Ljava/lang/String;Z)V")
    putInt = JavaMethod("(Ljava/lang/String;I)V")
    putLong = JavaMethod("(Ljava/lang/String;J)V")
    putDouble = JavaMethod("(Ljava/lang/String;D)V")
    putString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    putBooleanArray = JavaMethod("(Ljava/lang/String;[Z)V")
    putIntArray = JavaMethod("(Ljava/lang/String;[I)V")
    putLongArray = JavaMethod("(Ljava/lang/String;[J)V")
    putDoubleArray = JavaMethod("(Ljava/lang/String;[D)V")
    putStringArray = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;)V")
    getBoolean = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;Z)Z", False, False)])
    getInt = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;I)I", False, False)])
    getLong = JavaMultipleMethod([("(Ljava/lang/String;)J", False, False), ("(Ljava/lang/String;J)J", False, False)])
    getDouble = JavaMultipleMethod([("(Ljava/lang/String;)D", False, False), ("(Ljava/lang/String;D)D", False, False)])
    getString = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getBooleanArray = JavaMethod("(Ljava/lang/String;)[Z")
    getIntArray = JavaMethod("(Ljava/lang/String;)[I")
    getLongArray = JavaMethod("(Ljava/lang/String;)[J")
    getDoubleArray = JavaMethod("(Ljava/lang/String;)[D")
    getStringArray = JavaMethod("(Ljava/lang/String;)[Ljava/lang/String;")