from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseBundle"]

class BaseBundle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/BaseBundle"
    remove = JavaMethod("(Ljava/lang/String;)V")
    size = JavaMethod("()I")
    getBoolean = JavaMultipleMethod([("(Ljava/lang/String;Z)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])
    putBoolean = JavaMethod("(Ljava/lang/String;Z)V")
    getInt = JavaMultipleMethod([("(Ljava/lang/String;I)I", False, False), ("(Ljava/lang/String;)I", False, False)])
    putInt = JavaMethod("(Ljava/lang/String;I)V")
    getLong = JavaMultipleMethod([("(Ljava/lang/String;)J", False, False), ("(Ljava/lang/String;J)J", False, False)])
    putLong = JavaMethod("(Ljava/lang/String;J)V")
    getDouble = JavaMultipleMethod([("(Ljava/lang/String;D)D", False, False), ("(Ljava/lang/String;)D", False, False)])
    putDouble = JavaMethod("(Ljava/lang/String;D)V")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    get = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    putAll = JavaMethod("(Landroid/os/PersistableBundle;)V")
    keySet = JavaMethod("()Ljava/util/Set;")
    containsKey = JavaMethod("(Ljava/lang/String;)Z")
    getBooleanArray = JavaMethod("(Ljava/lang/String;)[Z")
    getLongArray = JavaMethod("(Ljava/lang/String;)[J")
    getString = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    putStringArray = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;)V")
    putString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    putLongArray = JavaMethod("(Ljava/lang/String;[J)V")
    putIntArray = JavaMethod("(Ljava/lang/String;[I)V")
    putDoubleArray = JavaMethod("(Ljava/lang/String;[D)V")
    putBooleanArray = JavaMethod("(Ljava/lang/String;[Z)V")
    getStringArray = JavaMethod("(Ljava/lang/String;)[Ljava/lang/String;")
    getIntArray = JavaMethod("(Ljava/lang/String;)[I")
    getDoubleArray = JavaMethod("(Ljava/lang/String;)[D")